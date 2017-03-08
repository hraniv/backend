from data.models import User
from data.schemas import UserSchema
from mixins.controllers import ListMixin


class UserResource(ListMixin):
    schema = UserSchema
    queryset = User.objects.all()

