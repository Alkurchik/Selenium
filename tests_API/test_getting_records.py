import requests
from ..configuration import SERVICE_URL
from ..src.json_entities_to_validate.records_jsonschema import RECORD_SCHEMA
from ..src.json_entities_to_validate.users_pydantic import ResponseGetUserValidator
from .base_classes.responses import Response, GetUserResponse
import allure


@allure.feature('GET_record')
@allure.story('API')
def test_getting_records():
    r = requests.get(f'{SERVICE_URL}users/2')
    response = Response(r)
    response.assert_status_code(200).validate(RECORD_SCHEMA)


@allure.feature('GET_User')
@allure.story('API')
def test_getting_user():
    r = requests.get(f'{SERVICE_URL}users/2')
    response = GetUserResponse(r)
    response.validate(ResponseGetUserValidator)
    response.assert_status_code(200)
