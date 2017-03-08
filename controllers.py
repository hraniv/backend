import json

from data.models import User
from data.schemas import UserSchema


class UserResource:
    schema = UserSchema

    def on_get(self, req, resp):

        resp.body = UserSchema().dumps(User.objects.first()).data
        # resp.data = {
        #     'quote': 'I\'ve always been more interested in the future than in the past.',
        #     'author': 'Grace Hopper'
        # }
