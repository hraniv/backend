import falcon
from django.core.exceptions import ValidationError


def call_model_full_clean(obj, model):
    try:
        obj.full_clean()
    except ValidationError as err:
        raise falcon.HTTPBadRequest('Invalid data', err.message_dict)


class ListMixin:
    # TODO add pagination

    def on_get(self, req, resp):
        resp.body = self.schema().dumps(self.get_queryset(), many=True).data


class CreateMixin:

    def on_post(self, req, resp):
        schema = self.schema()
        data, errors = schema.load(req.params)
        if errors:
            raise falcon.HTTPBadRequest('Invalid data', errors)

        new_obj = self.model()
        for key, value in data.items():
            setattr(new_obj, key, value)

        call_model_full_clean(new_obj, self.model)

        new_obj.save()

        resp.body = schema.dumps(new_obj).data


class RetrieveMixin:

    def on_get(self, req, resp, pk):
        resp.body = self.schema().dumps(self.get_object(pk)).data


class DestroyMixin:
    def on_delete(self, req, resp, pk):
        self.get_object(pk).delete()
        resp.status = falcon.HTTP_204


class UpdateMixin:
    def update_object(self, pk, params, resp, partial):
        schema = self.schema()
        data, errors = schema.load(params, partial=partial)
        if errors:
            raise falcon.HTTPBadRequest('Invalid data', errors)

        obj = self.get_object(pk)
        for (key, value) in data.items():
            setattr(obj, key, value)

        call_model_full_clean(obj, self.model)

        obj.save()

        resp.body = schema.dumps(obj).data

    def on_patch(self, req, resp, pk):
        self.update_object(pk, params=req.params, resp=resp, partial=True)

    def on_put(self, req, resp, pk):
        self.update_object(pk, params=req.params, resp=resp, partial=False)


# TODO check autogeneration of schema from model in marsh docs
