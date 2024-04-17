from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User
from qualities.models import Education

# Create your models here.
# Resume 
class Resume(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    summary = models.TextField(verbose_name='Summary', null=True, blank=True)
    education = models.ManyToManyField(Education, verbose_name='Education')
#     skills = models.TextField(verbose_name='Skills')
#     achievements = models.ManyToManyField(Achievement, verbose_name='Achievements')
#     projects = models.ManyToManyField(Project, verbose_name='Projects')
#     additional_sections = models.TextField(verbose_name='Additional Sections', blank=True)
#     work_experience = models.ForeignKey(WorkExperience, verbose_name='Work Experience', on_delete=models.CASCADE)
