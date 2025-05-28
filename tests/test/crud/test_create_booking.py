from Src.helpers.api_requests_wrapper import post_request
from Src.constants.api_constants import APIConstants
from Src.utils.utils import Util
from Src.helpers.payload_manager import *
from Src.helpers.common_verification import verify_status_codes,verify_json_key_for_not_null

import pytest
import allure

class TestCreateBooking(object):
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title('Verify that create booking status and Booking ID should not be empty')
    @allure.description('Creating a booking from payload and verify that booking id is not empty')
    def test_create_booking_positive(self):
        response=post_request(url=APIConstants.url_for_create_booking(),headers=Util().common_headers_json(),auth=None,payload=payload_create_booking(),in_json=False)
        booking_id=response.json()["bookingid"]
        verify_status_codes(response_data=response,expected_data=200)
        verify_json_key_for_not_null(booking_id)

    @pytest.mark.negative
    def test_create_booking_negative(self):
        response=post_request(url=APIConstants.url_for_create_booking(),headers=Util().common_headers_json(),auth=None,payload={},in_json=False)
        verify_status_codes(response_data=response,expected_data=500)
