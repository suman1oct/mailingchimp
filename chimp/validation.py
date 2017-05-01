from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_fullname(name):
	name_part = name.split()
	if len(name_part) < 2:
		raise ValidationError(_('{0} is not valid name, Please enter Full Name'.format(name)))


def validate_file_extension(value):
	pass


def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        raise ValidationError("Please enter a valid  email address")