from django.db import models
import uuid
from django.utils.text import slugify

# Hobby
class Hobby(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='slug', null=True, blank=True)



# Testimonial
class Testimonial(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, blank=True, null=True)
    source = models.CharField(verbose_name='Source', max_length=255)
    content = models.TextField(verbose_name='Content')
    date = models.DateField(verbose_name='Date')




# Work Experience
class WorkExperience(models.Model):
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, blank=True, null=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    position = models.CharField(verbose_name='Position', max_length=255)
    company = models.CharField(verbose_name='Company/Organization', max_length=255)
    location = models.CharField(verbose_name='Location', max_length=255)
    employment_duration = models.CharField(verbose_name='Employment Duration', max_length=255)
    responsibilities = models.TextField(verbose_name='Responsibilities')



# Project
class Project(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name='Project Name', max_length=255)
    description = models.TextField(verbose_name='Description', blank=True)
    start_date = models.DateField(verbose_name='Start Date', blank=True, null=True)
    end_date = models.DateField(verbose_name='End Date', blank=True, null=True)


# Achievement
class Achievement(models.Model):
    name = models.CharField(verbose_name='Achievement Name', max_length=255)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(verbose_name='Description', blank=True)
    date_achieved = models.DateField(verbose_name='Date Achieved', blank=True, null=True)
    related_project = models.ForeignKey(Project, verbose_name='Related Project', on_delete=models.CASCADE, blank=True, null=True)
    certificate_file = models.FileField(verbose_name='Certificate File', upload_to='certificates/', blank=True, null=True)


# Resume 
class Resume(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    personal_information = models.TextField(verbose_name='Personal Information')
    education = models.TextField(verbose_name='Education')
    skills = models.TextField(verbose_name='Skills')
    achievements = models.ManyToManyField(Achievement, verbose_name='Achievements')
    projects = models.ManyToManyField(Project, verbose_name='Projects')
    additional_sections = models.TextField(verbose_name='Additional Sections', blank=True)
    work_experience = models.ForeignKey(WorkExperience, verbose_name='Work Experience', on_delete=models.CASCADE)







