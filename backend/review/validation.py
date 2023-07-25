from django.core.exceptions import ValidationError

def validate_grade(value):
        if value <= 0 or value >5:
            raise ValidationError(f"Grade must be between 1 and 5")