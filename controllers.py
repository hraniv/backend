from data.models import User
from data.schemas import UserSchema
from mixins.controllers import ListMixin, DetailMixin


class UserListResource(ListMixin):
    schema = UserSchema
    model = User


class UserDetailResource(DetailMixin):
    schema = UserSchema
    model = User
