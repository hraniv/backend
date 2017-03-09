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
