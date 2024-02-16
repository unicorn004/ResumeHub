from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.
class Hobby(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='slug', null=True, blank=True)

    def save(self, *args, **kwargs):
        value = f'{self.name}'
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
