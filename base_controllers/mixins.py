from ujson import dumps

import falcon
from django.core.exceptions import ValidationError

from settings import DEFAULT_PAGE_SIZE, MAX_PER_PAGE


def call_model_full_clean(obj, model):
    try:
        obj.full_clean()
    except ValidationError as err:
        raise falcon.HTTPBadRequest('Invalid data', err.message_dict)


class PagePaginator:

    def paginate(self, queryset, page_size, req):
        page_num = req.get_param_as_int('page') or 1
        limit, offset = (page_num - 1) * page_size, page_num * page_size
        return queryset[limit:offset]


class ListMixin:
    paginator_class = PagePaginator
    page_size = None

    def get_page_size(self, req):
        page_size = req.get_param_as_int('page_size') or self.page_size or DEFAULT_PAGE_SIZE
        return min(page_size, MAX_PER_PAGE)

    def on_get(self, req, resp):
        qs = self.get_queryset()
        if self.paginator_class:
            qs = self.paginator_class().paginate(qs, self.get_page_size(req), req)
            resp.body = dumps({
                'objects_count': qs.count(),
                'data': self.schema().dump(qs, many=True).data,
            })

        else:
            resp.body = self.schema().dumps(qs, many=True).data


class CreateMixin:

    def on_post(self, req, resp):
        schema = self.schema()
        errors = schema.validate(req.params)
        if errors:
            raise falcon.HTTPBadRequest('Invalid data', errors)

        new_obj = self.model()
        for key, value in req.params.items():
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
        errors = schema.validate(params, partial=partial)
        if errors:
            raise falcon.HTTPBadRequest('Invalid data', errors)

        obj = self.get_object(pk)
        for (key, value) in params.items():
            setattr(obj, key, value)

        call_model_full_clean(obj, self.model)
        obj.save()
        resp.body = schema.dumps(obj).data

    def on_patch(self, req, resp, pk):
        self.update_object(pk, params=req.params, resp=resp, partial=True)

    def on_put(self, req, resp, pk):
        self.update_object(pk, params=req.params, resp=resp, partial=False)
