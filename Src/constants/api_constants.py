#API Constants -Class which contain all the endpoints
#keep URLs
#static method is used.

class APIConstants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_for_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_for_create_token():
        return "https://restful-booker.herokuapp.com/auth"


    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/"+str(booking_id)