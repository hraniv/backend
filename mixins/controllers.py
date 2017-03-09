import falcon


class BaseModelController:
    schema = None
    model = None

    def get_queryset(self):
        return self.model.objects.all()

    def get_object(self, pk):
        try:
            return self.get_queryset().get(pk=pk)
        except self.model.DoesNotExist:
            raise falcon.HTTPNotFound()


class ListMixin:
    # TODO add pagination

    def on_get(self, req, resp):
        resp.body = self.schema().dumps(self.get_queryset(), many=True).data


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
        obj.save()

        resp.body = schema.dumps(obj).data

    def on_patch(self, req, resp, pk):
        self.update_object(pk, params=req.params, resp=resp, partial=True)

    def on_put(self, req, resp, pk):
        self.update_object(pk, params=req.params, resp=resp, partial=False)


# TODO add post
# TODO add single object base mixin with with self.get_object

