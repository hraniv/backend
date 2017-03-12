from base_controllers.controllers import BaseModelResource
from db.models import User
from db.schemas import UserSchema
from base_controllers import mixins


class UserListResource(mixins.ListMixin,
                       mixins.CreateMixin,
                       BaseModelResource):
    schema = UserSchema
    model = User


class UserSingleResource(mixins.RetrieveMixin,
                         mixins.DestroyMixin,
                         mixins.UpdateMixin,
                         BaseModelResource):
    schema = UserSchema
    model = User
