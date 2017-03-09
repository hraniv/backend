import falcon

from data.schemas import UserSchema


class ListMixin:
    schema = None
    model = None
    # TODO add pagination

    def get_queryset(self):
        return self.model.objects.all()

    def on_get(self, req, resp):
        resp.body = UserSchema().dumps(self.get_queryset(), many=True).data


class DetailMixin:
    schema = None
    model = None

    def get_queryset(self):
        return self.model.objects.all()

    def on_get(self, req, resp, pk):
        try:
            item = self.get_queryset().get(pk=pk)
        except self.model.DoesNotExist:
            raise falcon.HTTPNotFound()
        else:
            resp.body = UserSchema().dumps(item).data

# TODO add post, put, patch mixins
