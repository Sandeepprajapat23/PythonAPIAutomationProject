from Src.constants.api_constants import APIConstants
from Src.helpers.api_requests_wrapper import *
from Src.helpers.common_verification import *
from Src.helpers.payload_manager import payload_create_booking,payload_create_token
from Src.utils.utils import Util

import allure
import pytest
import openpyxl


@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants.url_for_create_token(),
        headers=Util().common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json=False
    )
    verify_status_codes(response_data=response, expected_data=200)
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(url=APIConstants.url_for_create_booking(),
                            auth=None,
                            headers=Util().common_headers_json(),
                            payload=payload_create_booking(),
                            in_json=False)
    
    booking_id = response.json()["bookingid"]
    
    verify_status_codes(response_data=response,expected_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id


