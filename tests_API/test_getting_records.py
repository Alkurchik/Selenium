import requests
from ..configuration import SERVICE_URL
from ..src.json_entities_to_validate.records import RECORD_SCHEMA
from .base_classes.responses import Response
import allure


@allure.feature('GET_records')
@allure.story('API')
def test_getting_records():
    r = requests.get(f'{SERVICE_URL}users/2')
    response = Response(r)
    response.assert_status_code(400).validate(RECORD_SCHEMA)
