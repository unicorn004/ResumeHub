from django.db import models
from django.utils.text import slugify
import uuid
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.text import slugify

def validate_image(image):
    file_size = image.file.size
    limit_kb = 512
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)

class Company(models.Model):
    """
    Stores global configuration data of a company for the platform.
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='name', max_length=100, blank=False, unique=True)
    # show_name = models.BooleanField(verbose_name='show name on navbar', default=False)
    # show_logo = models.BooleanField(verbose_name='show logo on navbar', default=True)
    description = models.TextField(verbose_name='description', blank=True)
    address = models.TextField(verbose_name='address')
    email = models.EmailField(verbose_name='email')
    contact_numbers = models.CharField(verbose_name='contact_numbers', blank=True, max_length=100)

    def __str__(self):
        return self.name