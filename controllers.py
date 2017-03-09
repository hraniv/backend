from data.models import User
from data.schemas import UserSchema
from mixins.controllers import ListMixin, BaseModelController, RetrieveMixin, DestroyMixin, \
    UpdateMixin


class UserListResource(ListMixin, BaseModelController):
    schema = UserSchema
    model = User


class UserSingleResource(RetrieveMixin, DestroyMixin, UpdateMixin, BaseModelController):
    schema = UserSchema
    model = User
