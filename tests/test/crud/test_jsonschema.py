# Get Response
# Create the JSON schema - https://www.jsonschema.net/
# Save that schema into the name.json file
# If you want to validate the json schema - https://www.jsonschemavalidator.net/
import json
import os

import allure
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from Src.constants.api_constants import APIConstants
from Src.helpers.api_requests_wrapper import post_request
from Src.helpers.common_verification import *
from Src.helpers.payload_manager import payload_create_booking
from Src.utils.utils import Util


class TestCreateBookingJSONSchema(object):
    
    def load_schema(self, file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the paylaod and verfiy that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_schema(self):
        response = post_request(url=APIConstants.url_for_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)
        
        booking_id = response.json()["bookingid"]
        
        verify_status_codes(response_data=response,expected_data=200)
        verify_json_key_for_not_null(booking_id)
        
        # response with schema.json stored
        file_path = os.getcwd() + "/create_schema.json"
        schema = self.load_schema(file_name=file_path)
        
        try:
            validate(instance=response.json(), schema=schema)
        except ValidationError as e:
            print(e.message)
            pytest.fail("Failed : JSON schema error")
