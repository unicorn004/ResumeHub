from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User
from qualities.models import Education
from companies.models import Company

# Create your models here.
# Resume 
class Resume(models.Model):
    """
    Holds Resume created by the candidate.
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(verbose_name='slug', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    summary = models.TextField(verbose_name='Summary', null=True, blank=True)
    
    # Education level choices
    education = models.PositiveSmallIntegerField('Educational qualifications (recent N, 0 for none)', default=0)

    # Options
    include_address = models.BooleanField(verbose_name='Include Address', default=True)
    include_contact_number = models.BooleanField(verbose_name='Include Contact Number', default=True)
    include_email_id = models.BooleanField(verbose_name='Include Email ID', default=True)
    target_company = models.ManyToManyField(Company, verbose_name='Target Companies')

#     skills = models.TextField(verbose_name='Skills')
#     achievements = models.ManyToManyField(Achievement, verbose_name='Achievements')
#     projects = models.ManyToManyField(Project, verbose_name='Projects')
#     additional_sections = models.TextField(verbose_name='Additional Sections', blank=True)
#     work_experience = models.ForeignKey(WorkExperience, verbose_name='Work Experience', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
            value = self.unique_id
            self.slug = slugify(value, allow_unicode=True)
            super().save(*args, **kwargs)

