from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def validate_fullname(name):
	name_part = name.split()
	if len(name_part) < 2:
		raise ValidationError(_('{0} is not valid name, Please enter Full Name'.format(name)))



def validateEmail( email ):
    
    try:
        validate_email( email )
        return True
    except ValidationError:
        raise ValidationError("Please enter a valid  email address")


def validate_file_extension(file):
	pass
	

