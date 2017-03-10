from django.core.wsgi import get_wsgi_application
from falcon import RequestOptions

get_wsgi_application()

import falcon
from controllers import UserListResource, UserSingleResource

api = falcon.API()
api.req_options = RequestOptions()
api.req_options.auto_parse_form_urlencoded = True
# TODO check if there is a way to set these ^ settings properly

api.add_route('/users/', UserListResource())
api.add_route('/users/{pk}/', UserSingleResource())
