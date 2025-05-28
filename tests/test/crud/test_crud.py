import pytest
import allure

from Src.helpers.payload_manager import *
from Src.helpers.api_requests_wrapper import *
from Src.utils.utils import Util
from Src.constants.api_constants import APIConstants
from Src.helpers.common_verification import *

class TestCrud(object):
    @pytest.fixture()
    def create_booking(self):
        response=post_request(url=APIConstants.url_for_create_booking(),headers=Util().common_headers_json(),auth=None,payload=payload_create_booking(),in_json=False)
        booking_id=response.json()["bookingid"]
        return booking_id

    @pytest.fixture()
    def create_token(self):
        response=post_request(url=APIConstants.url_for_create_token(),headers=Util().common_headers_json(),auth=None,payload=payload_create_token(),in_json=False)
        token=response.json()["token"]
        return token

    @pytest.mark.positive
    def test_update_booking(self,create_booking,create_token):
        booking_id=create_booking
        token=create_token
        put_response=put_request(url=APIConstants.url_patch_put_delete(booking_id=booking_id),headers=Util().common_header_put_patch_delete_with_basic_cookie(token=token),auth=None,payload=payload_create_booking_dynamic(),in_json=False)
        print(put_response.json())
        verify_status_codes(response_data=put_response,expected_data=200)
        verify_key_response_not_be_none(key='firstname')
        verify_json_key_for_not_null(put_response.json()["firstname"])

    @pytest.mark.positive
    def test_delete_booking(self,create_booking,create_token):
        booking_id=create_booking
        token=create_token
        delete_response=delete_request(url=APIConstants.url_patch_put_delete(booking_id=booking_id),headers=Util().common_header_put_patch_delete_with_basic_cookie(token=token),auth=None,in_json=False)
        print(delete_response.text)
        verify_status_codes(response_data=delete_response,expected_data=201)