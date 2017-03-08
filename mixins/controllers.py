from data.schemas import UserSchema


class ListMixin:
    schema = None
    queryset = None

    def get_queryset(self):
        return self.queryset

    def on_get(self, req, resp):
        resp.body = UserSchema().dumps(self.get_queryset(), many=True).data
