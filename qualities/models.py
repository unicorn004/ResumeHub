from django.db import models
import uuid
from django.utils.text import slugify

class Hobby(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)

    def save(self, *args, **kwargs):
        value = f'{self.name}'
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Skill(models.Model):
    TECHNICAL = 'technical'
    SOFT = 'soft'
    SKILL_TYPES = [
        (TECHNICAL, 'Technical Skill'),
        (SOFT, 'Soft Skill')
    ]

    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)
    skill_type = models.CharField(verbose_name='Type', max_length=10, choices=SKILL_TYPES)
    
    # Attributes specific to technical skills
    programming_languages = models.BooleanField(verbose_name='Programming Languages', default=False)
    frameworks = models.BooleanField(verbose_name='Frameworks and Libraries', default=False)
    version_control = models.BooleanField(verbose_name='Version Control Systems', default=False)
    methodologies = models.BooleanField(verbose_name='Development Methodologies', default=False)
    data_analysis = models.BooleanField(verbose_name='Data Analysis and Analytics', default=False)
    it_networking = models.BooleanField(verbose_name='IT and Networking', default=False)
    web_dev_design = models.BooleanField(verbose_name='Web Development and Design', default=False)
    ai_ml = models.BooleanField(verbose_name='Machine Learning and Artificial Intelligence', default=False)
    dbms = models.BooleanField(verbose_name='Database Management', default=False)
    cloud_computing = models.BooleanField(verbose_name='Cloud Computing', default=False)

    # Attributes specific to soft skills
    communication = models.BooleanField(verbose_name='Communication', default=False)
    teamwork = models.BooleanField(verbose_name='Teamwork', default=False)
    leadership = models.BooleanField(verbose_name='Leadership', default=False)
    problem_solving = models.BooleanField(verbose_name='Problem Solving', default=False)
    adaptability = models.BooleanField(verbose_name='Adaptability', default=False)
    time_management = models.BooleanField(verbose_name='Time Management', default=False)

    description = models.TextField(verbose_name='Description', blank=True, null=True)

    def save(self, *args, **kwargs):
        value = f'{self.name}'
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)