from base_controllers.controllers import SingleModelResource, ListModelResource
from db.models import User
from db.schemas import UserSchema


class UserListResource(ListModelResource):
    schema = UserSchema
    model = User


class UserSingleResource(SingleModelResource):
    schema = UserSchema
    model = User
