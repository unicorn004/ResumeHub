from django.db import models
import uuid
from django.utils.text import slugify

# Hobby
class Hobby(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='slug', null=True, blank=True)

    def save(self, *args, **kwargs):
        value = f'{self.name}'
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


# Testimonial
class Testimonial(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    source = models.CharField(verbose_name='Source', max_length=255)
    content = models.TextField(verbose_name='Content')
    date = models.DateField(verbose_name='Date')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


# Work Experience
class WorkExperience(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    position = models.CharField(verbose_name='Position', max_length=255)
    company = models.CharField(verbose_name='Company/Organization', max_length=255)
    location = models.CharField(verbose_name='Location', max_length=255)
    employment_duration = models.CharField(verbose_name='Employment Duration', max_length=255)
    responsibilities = models.TextField(verbose_name='Responsibilities')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


# Resume
class Resume(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    personal_information = models.TextField(verbose_name='Personal Information')
    education = models.TextField(verbose_name='Education')
    skills = models.TextField(verbose_name='Skills')
    work_experience = models.TextField(verbose_name='Work Experience')
    achievements = models.TextField(verbose_name='Achievements')
    projects = models.TextField(verbose_name='Projects')
    additional_sections = models.TextField(verbose_name='Additional Sections', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)




