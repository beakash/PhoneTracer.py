import phonenumbers
from phonenumbers import geocoder
import time

class PhoneTracer:
    def __init__(self):
        self.version = "2.1"
        
    def trace(self, phone_number):
        """Trace a phone number's location."""
        try:
            # Parse the phone number
            parsed_number = phonenumbers.parse(phone_number, None)
            
            # Get the location description
            location = geocoder.description_for_number(parsed_number, "en")
            
            return {
                'number': phone_number,
                'valid': True,
                'location': location,
                'carrier': None  # Can be implemented later
            }
        except phonenumbers.NumberParseException as e:
            return {
                'number': phone_number,
                'valid': False,
                'error': str(e)
            }
