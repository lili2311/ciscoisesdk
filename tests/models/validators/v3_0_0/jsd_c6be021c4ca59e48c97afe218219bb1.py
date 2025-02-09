# -*- coding: utf-8 -*-
"""Identity Services Engine getActiveDirectoryByName data model.

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


class JSONSchemaValidatorC6Be021C4Ca59E48C97Afe218219Bb1(object):
    """getActiveDirectoryByName request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC6Be021C4Ca59E48C97Afe218219Bb1, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "ERSActiveDirectory": {
                "properties": {
                "adAttributes": {
                "properties": {
                "attributes": {
                "items": {
                "properties": {
                "defaultValue": {
                "type": "string"
                },
                "internalName": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "adScopesNames": {
                "type": "string"
                },
                "adgroups": {
                "properties": {
                "groups": {
                "items": {
                "properties": {
                "name": {
                "type": "string"
                },
                "sid": {
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "advancedSettings": {
                "properties": {
                "agingTime": {
                "type": "integer"
                },
                "country": {
                "type": "string"
                },
                "department": {
                "type": "string"
                },
                "email": {
                "type": "string"
                },
                "enableCallbackForDialinClient": {
                "type": "boolean"
                },
                "enableDialinPermissionCheck": {
                "type": "boolean"
                },
                "enableMachineAccess": {
                "type": "boolean"
                },
                "enableMachineAuth": {
                "type": "boolean"
                },
                "enablePassChange": {
                "type": "boolean"
                },
                "enableRewrites": {
                "type": "boolean"
                },
                "firstName": {
                "type": "string"
                },
                "identityNotInAdBehaviour": {
                "type": "string"
                },
                "jobTitle": {
                "type": "string"
                },
                "lastName": {
                "type": "string"
                },
                "locality": {
                "type": "string"
                },
                "organizationalUnit": {
                "type": "string"
                },
                "plaintextAuth": {
                "type": "boolean"
                },
                "rewriteRules": {
                "items": {
                "properties": {
                "rewriteMatch": {
                "type": "string"
                },
                "rewriteResult": {
                "type": "string"
                },
                "rowId": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "schema": {
                "type": "string"
                },
                "stateOrProvince": {
                "type": "string"
                },
                "streetAddress": {
                "type": "string"
                },
                "telephone": {
                "type": "string"
                },
                "unreachableDomainsBehaviour": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "description":
                 {
                "type": "string"
                },
                "domain": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "required": [
                "name",
                "domain"
                ],
                "type": "object"
                }
                },
                "required": [
                "ERSActiveDirectory"
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
