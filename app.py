from django.core.wsgi import get_wsgi_application

get_wsgi_application()

import falcon

from middlewares import TokenAuthentication
from controllers import UserListResource, UserSingleResource


api = falcon.API(middleware=TokenAuthentication())
api.req_options = falcon.RequestOptions()
api.req_options.auto_parse_form_urlencoded = True
# TODO check if there is a way to set these ^ settings properly


api.add_route('/users/', UserListResource())
api.add_route('/users/{pk}/', UserSingleResource())
