# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI backup_and_restore API fixtures and tests.

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


def is_valid_config_backup(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_0740db1d9dda53369e35d33138b29c16_v3_0_0').validate(obj.response)
    return True


def config_backup(api):
    endpoint_result = api.backup_and_restore.config_backup(
        active_validation=False,
        backup_encryption_key='string',
        backup_name='string',
        payload=None,
        repository_name='string'
    )
    return endpoint_result


@pytest.mark.backup_and_restore
def test_config_backup(api, validator):
    try:
        assert is_valid_config_backup(
            validator,
            config_backup(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def config_backup_default(api):
    endpoint_result = api.backup_and_restore.config_backup(
        active_validation=False,
        backup_encryption_key=None,
        backup_name=None,
        payload=None,
        repository_name=None
    )
    return endpoint_result


@pytest.mark.backup_and_restore
def test_config_backup_default(api, validator):
    try:
        assert is_valid_config_backup(
            validator,
            config_backup_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_restore_config_backup(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_b8319a8b5d195348a8763acd95ca2967_v3_0_0').validate(obj.response)
    return True


def restore_config_backup(api):
    endpoint_result = api.backup_and_restore.restore_config_backup(
        active_validation=False,
        backup_encryption_key='string',
        payload=None,
        repository_name='string',
        restore_file='string',
        restore_include_adeos='string'
    )
    return endpoint_result


@pytest.mark.backup_and_restore
def test_restore_config_backup(api, validator):
    try:
        assert is_valid_restore_config_backup(
            validator,
            restore_config_backup(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def restore_config_backup_default(api):
    endpoint_result = api.backup_and_restore.restore_config_backup(
        active_validation=False,
        backup_encryption_key=None,
        payload=None,
        repository_name=None,
        restore_file=None,
        restore_include_adeos=None
    )
    return endpoint_result


@pytest.mark.backup_and_restore
def test_restore_config_backup_default(api, validator):
    try:
        assert is_valid_restore_config_backup(
            validator,
            restore_config_backup_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_cancel_backup(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3e155669bc74586e9ef2580ec5752902_v3_0_0').validate(obj.response)
    return True


def cancel_backup(api):
    endpoint_result = api.backup_and_restore.cancel_backup(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.backup_and_restore
def test_cancel_backup(api, validator):
    try:
        assert is_valid_cancel_backup(
            validator,
            cancel_backup(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def cancel_backup_default(api):
    endpoint_result = api.backup_and_restore.cancel_backup(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.backup_and_restore
def test_cancel_backup_default(api, validator):
    try:
        assert is_valid_cancel_backup(
            validator,
            cancel_backup_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_last_config_backup_status(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d388e26255a15233ac682c0406880cfb_v3_0_0').validate(obj.response)
    return True


def get_last_config_backup_status(api):
    endpoint_result = api.backup_and_restore.get_last_config_backup_status(

    )
    return endpoint_result


@pytest.mark.backup_and_restore
def test_get_last_config_backup_status(api, validator):
    try:
        assert is_valid_get_last_config_backup_status(
            validator,
            get_last_config_backup_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_last_config_backup_status_default(api):
    endpoint_result = api.backup_and_restore.get_last_config_backup_status(

    )
    return endpoint_result


@pytest.mark.backup_and_restore
def test_get_last_config_backup_status_default(api, validator):
    try:
        assert is_valid_get_last_config_backup_status(
            validator,
            get_last_config_backup_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_schedule_config_backup(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_2b994e6c8b8d53f29230686824c9fafa_v3_0_0').validate(obj.response)
    return True


def schedule_config_backup(api):
    endpoint_result = api.backup_and_restore.schedule_config_backup(
        active_validation=False,
        backup_description='string',
        backup_encryption_key='string',
        backup_name='string',
        end_date='string',
        frequency='string',
        payload=None,
        repository_name='string',
        start_date='string',
        time='string'
    )
    return endpoint_result


@pytest.mark.backup_and_restore
def test_schedule_config_backup(api, validator):
    try:
        assert is_valid_schedule_config_backup(
            validator,
            schedule_config_backup(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def schedule_config_backup_default(api):
    endpoint_result = api.backup_and_restore.schedule_config_backup(
        active_validation=False,
        backup_description=None,
        backup_encryption_key=None,
        backup_name=None,
        end_date=None,
        frequency=None,
        payload=None,
        repository_name=None,
        start_date=None,
        time=None
    )
    return endpoint_result


@pytest.mark.backup_and_restore
def test_schedule_config_backup_default(api, validator):
    try:
        assert is_valid_schedule_config_backup(
            validator,
            schedule_config_backup_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
