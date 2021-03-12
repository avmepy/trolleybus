#!/usr/bin/env python3
# -*-encoding: utf-8-*-

import json
from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):

        errors = data.get('errors', None)

        # If we receive the token as part of the response, it will be byte
        # an object. Byte objects do not serialize well, so we need
        # decode them before rendering the User object.
        token = data.get('token', None)

        if errors is not None:
            return super(UserJSONRenderer, self).render(data)

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        # Finally, we can display our data in the 'user' namespace.
        return json.dumps({
            'user': data
        })
