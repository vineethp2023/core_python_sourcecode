import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

phno  = input("Enter a phone number with country code: ")
#parsing the string to the phone number
phone_number =phonenumbers.parse(phno)
#calculating time zone and displaying
time_zone = timezone.time_zones_for_number(phone_number)
print('Time zone of the given phone number is: ',str(time_zone))
# finding geographic region of phone number , here en is the language English, we can set hi for Hindi and ml for Malayalam
geo_loc = geocoder.description_for_number(phone_number,'en')
print('The geographic information about the given phone number is ',geo_loc)
# obtaining service provider's info
sp = carrier.name_for_number(phone_number,'en')
print('Service provider\'s name of the given number is: ',sp)