from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_fullname(name):
	name_part = name.split()
	if len(name_part) < 2:
		raise ValidationError(_('{0} is not valid name, Please enter Full Name'.format(name)))