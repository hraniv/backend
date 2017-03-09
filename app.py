from django.core.wsgi import get_wsgi_application
get_wsgi_application()

import falcon
from controllers import UserListResource, UserDetailResource
from middlewares import JSONMiddleware


api = falcon.API(middleware=JSONMiddleware())
api.add_route('/', UserListResource())
api.add_route('/{pk}/', UserDetailResource())
