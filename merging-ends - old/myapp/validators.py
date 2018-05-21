"""
This file contains methods for validating form input.
"""
from django import forms


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
