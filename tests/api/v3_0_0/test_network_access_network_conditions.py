# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI network_access_network_conditions API fixtures and tests.

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
import pytest
from fastjsonschema.exceptions import JsonSchemaException
from ciscoisesdk.exceptions import MalformedRequest
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_all_network_access_network_conditions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d43fec9e7dc556cbb9bf0ebd1dcd6aad_v3_0_0').validate(obj.response)
    return True


def get_all_network_access_network_conditions(api):
    endpoint_result = api.network_access_network_conditions.get_all_network_access_network_conditions(

    )
    return endpoint_result


@pytest.mark.network_access_network_conditions
def test_get_all_network_access_network_conditions(api, validator):
    try:
        assert is_valid_get_all_network_access_network_conditions(
            validator,
            get_all_network_access_network_conditions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_network_access_network_conditions_default(api):
    endpoint_result = api.network_access_network_conditions.get_all_network_access_network_conditions(

    )
    return endpoint_result


@pytest.mark.network_access_network_conditions
def test_get_all_network_access_network_conditions_default(api, validator):
    try:
        assert is_valid_get_all_network_access_network_conditions(
            validator,
            get_all_network_access_network_conditions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network_access_network_condition(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_f4dbfb874b3b56d7a651d6732f1bd55e_v3_0_0').validate(obj.response)
    return True


def create_network_access_network_condition(api):
    endpoint_result = api.network_access_network_conditions.create_network_access_network_condition(
        active_validation=False,
        condition_type='string',
        conditions=[{'ipAddrList': ['string'], 'macAddrList': ['string'], 'cliDnisList': ['string'], 'deviceList': ['string'], 'deviceGroupList': ['string']}],
        description='string',
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_network_conditions
def test_create_network_access_network_condition(api, validator):
    try:
        assert is_valid_create_network_access_network_condition(
            validator,
            create_network_access_network_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_network_access_network_condition_default(api):
    endpoint_result = api.network_access_network_conditions.create_network_access_network_condition(
        active_validation=False,
        condition_type=None,
        conditions=None,
        description=None,
        id=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_network_conditions
def test_create_network_access_network_condition_default(api, validator):
    try:
        assert is_valid_create_network_access_network_condition(
            validator,
            create_network_access_network_condition_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_access_network_condition_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_0ab015a9eb6d5f2b91002af068cb4ce2_v3_0_0').validate(obj.response)
    return True


def get_network_access_network_condition_by_id(api):
    endpoint_result = api.network_access_network_conditions.get_network_access_network_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_network_conditions
def test_get_network_access_network_condition_by_id(api, validator):
    try:
        assert is_valid_get_network_access_network_condition_by_id(
            validator,
            get_network_access_network_condition_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_access_network_condition_by_id_default(api):
    endpoint_result = api.network_access_network_conditions.get_network_access_network_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_network_conditions
def test_get_network_access_network_condition_by_id_default(api, validator):
    try:
        assert is_valid_get_network_access_network_condition_by_id(
            validator,
            get_network_access_network_condition_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network_access_network_condition_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_49780cf65cd559628b26f6eb5ea20f14_v3_0_0').validate(obj.response)
    return True


def update_network_access_network_condition_by_id(api):
    endpoint_result = api.network_access_network_conditions.update_network_access_network_condition_by_id(
        active_validation=False,
        condition_type='string',
        conditions=[{'ipAddrList': ['string'], 'macAddrList': ['string'], 'cliDnisList': ['string'], 'deviceList': ['string'], 'deviceGroupList': ['string']}],
        description='string',
        id='string',
        name='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_network_conditions
def test_update_network_access_network_condition_by_id(api, validator):
    try:
        assert is_valid_update_network_access_network_condition_by_id(
            validator,
            update_network_access_network_condition_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_network_access_network_condition_by_id_default(api):
    endpoint_result = api.network_access_network_conditions.update_network_access_network_condition_by_id(
        active_validation=False,
        id='string',
        condition_type=None,
        conditions=None,
        description=None,
        name=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.network_access_network_conditions
def test_update_network_access_network_condition_by_id_default(api, validator):
    try:
        assert is_valid_update_network_access_network_condition_by_id(
            validator,
            update_network_access_network_condition_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_network_access_network_condition_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_95e92c6e47625711b9ce06f92bd4d219_v3_0_0').validate(obj.response)
    return True


def delete_network_access_network_condition_by_id(api):
    endpoint_result = api.network_access_network_conditions.delete_network_access_network_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_network_conditions
def test_delete_network_access_network_condition_by_id(api, validator):
    try:
        assert is_valid_delete_network_access_network_condition_by_id(
            validator,
            delete_network_access_network_condition_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_network_access_network_condition_by_id_default(api):
    endpoint_result = api.network_access_network_conditions.delete_network_access_network_condition_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_access_network_conditions
def test_delete_network_access_network_condition_by_id_default(api, validator):
    try:
        assert is_valid_delete_network_access_network_condition_by_id(
            validator,
            delete_network_access_network_condition_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
