import phonenumbers
from phonenumbers import geocoder
pn1 = phonenumbers.parse('+18329213520')
print('phone number details')
print(geocoder.description_for_number(pn1,"en"))
