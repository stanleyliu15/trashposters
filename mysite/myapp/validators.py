"""
This file contains methods for validating form input.
"""
from django import forms


def validate_image_file(value):
    import os
    extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if extension not in valid_extensions:
        raise forms.ValidationError(u'An image file is required. (.jpg and .png file extensions only)')


def validate_address(value):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    try:
        location = geolocator.geocode(value)
        location.latitude
    except Exception as e:
        raise forms.ValidationError("This location is invalid. Please enter a valid address.")
