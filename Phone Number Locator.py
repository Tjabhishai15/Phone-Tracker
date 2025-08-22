import phonenumbers
from phonenumbers import geocoder, carrier

def locate_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(parsed_number):
            raise phonenumbers.phonenumberutil.NumberParseException("Invalid phone number.")
        country = geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")
        return f"The phone number is registered in {country} and is provided by {carrier_name}."
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return str(e)

# Example usage:
phone_number = input("Enter the phone number: ")
result = locate_number(phone_number)
print(result)