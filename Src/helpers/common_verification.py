def verify_status_codes(response_data,expected_data):
    assert response_data.status_code == expected_data

def verify_json_key_for_not_null(key):
    assert key!=0

def verify_key_response_not_be_none(key):
    assert key is not None

def verify_response_delete(response):
    assert "Created" in response

def verify_response_key(key, expected_data):
    assert key == expected_data
#common verification
#HTTP status code
#Headers
#Data Verification
#json schema