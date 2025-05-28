from faker import Faker
import json

faker=Faker()

def payload_create_booking():
    payload = {
        "firstname": "Amit",
        "lastname": "Sharma",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01",
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_booking_dynamic():
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01",
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "Wifi"))
    }
    return payload

def payload_create_token():
    payload = {
         "username": "admin",
        "password": "password123"
    }
    return payload

# def payload_create_booking_from_excel_json():
#     payload = {
#         "firstname":read_from_excel["firstname"],
#     }

