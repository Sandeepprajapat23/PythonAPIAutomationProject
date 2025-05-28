# Create Token
# Create Booking Id
# Update the Booking(Put) - BookingID, Token
# Delete the Booking

# Verify that created booking id when we update we are able to update it and delete it also

# create token
# create booking
# test_update() -> concept?
# fixtures -> pass the data in pytest

import allure
import pytest
import logging


from Src.constants.api_constants import APIConstants
from Src.helpers.api_requests_wrapper import *
from Src.helpers.common_verification import *
from Src.helpers.payload_manager import payload_create_booking
from Src.utils.utils import Util


class TestCRUDBooking(object):
    
    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working.")
    def test_update_booking_id_token(self,create_token,get_booking_id):
        logging.basicConfig(level=logging.INFO)
        logger  = logging.getLogger(__name__)
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_request(
            url=put_url,
            headers=Util().common_header_put_patch_delete_with_basic_cookie(token=token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )
        logger.info("Request is made"+ str(response))
        # Verification here & more
        verify_response_key(response.json()["firstname"],"Amit")
        verify_response_key(response.json()["lastname"],"Sharma")
        verify_status_codes(response_data=response,expected_data=200)
        logger.info("Request status code" + str(response.status_code))
        
    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description(
        "Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id(self,create_token,get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_request(
            url=delete_url,
            headers=Util().common_header_put_patch_delete_with_basic_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_response_delete(response=response.text)
        verify_status_codes(response_data=response,expected_data=201)
