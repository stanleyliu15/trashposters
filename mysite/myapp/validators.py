"""
This file contains methods for validating form input.
"""
from django import forms

STATES = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def validate_image_file(value):
    """
    Validator to check if an file in a form is an image file before allowing uploading to occur.
    :param      The file to check
    :return:    None
    :raise      ValidationError
    """
    import os
    extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if extension not in valid_extensions:
        raise forms.ValidationError(u'An image file is required. (.jpg and .png file extensions only)')


def validate_address(value):
    """
    Validator to check if address is valid before allowing post upload. Tries to access the latitude
    attribute of the address after geocoding it. If an error occurs, the geocoding failed.
    :param      The address to check
    :return:    None
    :raise      ValidationError
    """
    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    try:
        location = geolocator.geocode(value)
        location.latitude
    except Exception as e:
        raise forms.ValidationError("This location is invalid. Please enter a valid address.")


def validate_city(value):
    """
    Checks to see if a valid city has been provided. Works for non-Murican cities as well.
    If we can't convert it in a longitude and latutide, it probably doesn't
    exist.
    :param      value:  A city
    :return:    None
    :raise      ValidationError
    """
    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    try:
        location = geolocator.geocode(value)
        location.latitude
    except Exception as e:
        raise forms.ValidationError("Please enter a valid city name.")


def validate_state(value):
    """
    Checks to see if a valid US state has been provided. Murica.
    :param      value:  A US state
    :return:    None
    :raise      ValidationError
    """
    if value in STATES.values():
        return
    else:
        raise forms.ValidationError("Please enter a valid US state.")
