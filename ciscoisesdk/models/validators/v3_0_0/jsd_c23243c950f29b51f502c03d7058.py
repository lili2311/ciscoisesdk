# -*- coding: utf-8 -*-
"""Identity Services Engine createRestIdStore data model.

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


class JSONSchemaValidatorC23243C950F29B51F502C03D7058(object):
    """createRestIdStore request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC23243C950F29B51F502C03D7058, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "ERSRestIDStore": {
                "properties": {
                "description":
                 {
                "type": "string"
                },
                "ersRestIDStoreAttributes": {
                "properties": {
                "headers": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "required": [
                "key",
                "value"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "predefined": {
                "type": "string"
                },
                "rootUrl": {
                "type": "string"
                },
                "usernameSuffix": {
                "type": "string"
                }
                },
                "required": [
                "usernameSuffix",
                "rootUrl",
                "predefined",
                "headers"
                ],
                "type": "object"
                },
                "name": {
                "type": "string"
                }
                },
                "required": [
                "name",
                "ersRestIDStoreAttributes"
                ],
                "type": "object"
                }
                },
                "required": [
                "ERSRestIDStore"
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
