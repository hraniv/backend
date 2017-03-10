from django.core.wsgi import get_wsgi_application
from falcon import RequestOptions

get_wsgi_application()

import falcon
from controllers import UserListResource, UserSingleResource

api = falcon.API()
request_options = RequestOptions()
request_options.auto_parse_form_urlencoded = True
api.req_options = request_options

api.add_route('/users/', UserListResource())
api.add_route('/users/{pk}/', UserSingleResource())
