import json

import falcon


class JSONMiddleware(object):
    # Middleware example:
    # https://github.com/AndreiRegiani/falcon-jsonify/blob/master/falcon_jsonify/__init__.py

    # Middleware doc:
    # http://falcon.readthedocs.io/en/stable/api/middleware.html

    def process_request(self, req, resp):
        if not req.content_length:
            return

        body = req.stream.read()
        req.json = {}

        try:
            req.json = json.loads(body.decode('utf-8'))

        except ValueError:
            raise falcon.HTTPBadRequest('Malformed JSON', 'Syntax error')

        except UnicodeDecodeError:
            raise falcon.HTTPBadRequest('Invalid encoding', 'Could not decode as UTF-8')

    # def process_response(self, req, resp, resource, req_succeeded):
    #     resp.body = json.dumps(resp.data)
