# -*- coding: utf-8 -*-
"""Identity Services Engine getInternalUserByName data model.

Copyright (c) 2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from ciscoisesdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorF403Dda9440503191536993F569Cc6F(object):
    """getInternalUserByName request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorF403Dda9440503191536993F569Cc6F, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "InternalUser": {
                "properties": {
                "changePassword": {
                "type": "boolean"
                },
                "customAttributes": {
                "properties": {
                "Country": {
                "type": "string"
                },
                "Created": {
                "type": "string"
                },
                "Department": {
                "type": "string"
                },
                "Expired": {
                "type": "string"
                }
                },
                "required": [
                "Created",
                "Department",
                "Expired",
                "Country"
                ],
                "type": "object"
                },
                "description":
                 {
                "type": "string"
                },
                "enablePassword": {
                "type": "string"
                },
                "enabled": {
                "type": "boolean"
                },
                "expiryDateEnabled": {
                "type": "boolean"
                },
                "id": {
                "type": "string"
                },
                "link": {
                "properties": {
                "href": {
                "type": "string"
                },
                "rel": {
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "required": [
                "rel",
                "href",
                "type"
                ],
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "password": {
                "type": "string"
                },
                "passwordIDStore": {
                "type": "string"
                }
                },
                "required": [
                "id",
                "name",
                "description",
                "enabled",
                "password",
                "changePassword",
                "expiryDateEnabled",
                "enablePassword",
                "customAttributes",
                "passwordIDStore",
                "link"
                ],
                "type": "object"
                }
                },
                "required": [
                "InternalUser"
                ],
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
