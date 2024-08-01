from django.core.exceptions import ValidationError


def rating_validator(rating):
    if not (0.0 <= rating <= 10.0):
        raise ValidationError("The rating must be between 0.0 and 10.0")


def release_year_validator(rel_year):
    if not (1990 <= rel_year <= 2023):
        raise ValidationError("The release year must be between 1990 and 2023")
