from base_controllers.controllers import BaseModelController
from data.models import User
from data.schemas import UserSchema
from base_controllers import mixins


class UserListResource(mixins.ListMixin,
                       mixins.CreateMixin,
                       BaseModelController):
    schema = UserSchema
    model = User


class UserSingleResource(mixins.RetrieveMixin,
                         mixins.DestroyMixin,
                         mixins.UpdateMixin,
                         BaseModelController):
    schema = UserSchema
    model = User
