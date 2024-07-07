from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_image_extension(value):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    extension = os.path.splitext(value.name)[1]
    if extension.lower() not in valid_extensions:
        raise ValidationError(_('Unsupported file extension. Only .jpg, .jpeg, .png, .gif files are allowed.'))
