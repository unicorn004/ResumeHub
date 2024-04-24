from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User
from qualities.models import Education
from qualities.models import TechnicalSkill,SoftSkill
from companies.models import Company


class TechnicalSkill(models.Model):
    programming_language = 'programming_language'
    frameworks = 'frameworks'
    version_control = 'version_control'
    methodologies = 'methodologies'
    data_analysis = 'data_analysis'
    it_networking = 'it_networking'
    web_dev_design = 'web_dev_design'
    ai_ml = 'ai_ml'
    dbms = 'dbms'
    cloud_computing = 'cloud_computing'
    devops = 'devops'
    other= 'other'

    CATEGORY_CHOICES = [
        (programming_language, 'Programming Language'),
        (frameworks, 'Frameworks and Libraries'),
        (version_control, 'Version Control Systems'),
        (methodologies, 'Development Methodologies'),
        (data_analysis, 'Data Analysis and Analytics'),
        (it_networking, 'IT and Networking'),
        (web_dev_design, 'Web Development and Design'),
        (ai_ml, 'Machine Learning and Artificial Intelligence'),
        (dbms, 'Database Management'),
        (cloud_computing, 'Cloud Computing'),
        (devops, 'DevOps'),
        (other, 'Other')
    ]

    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)
    category = models.CharField(verbose_name='Category', max_length=25, choices=CATEGORY_CHOICES, default=other)
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.skill_type} - {self.category}'



class SoftSkill(models.Model):
    team_management = 'team_management'
    communication = 'communication'
    leadership = 'leadership'
    problem_solving = 'problem_solving'
    adaptability = 'adaptability'
    time_management = 'time_management'
    conflict_resolution = 'conflict_resolution'
    teamwork = 'teamwork'
    negotiation = 'negotiation'
    creativity = 'creativity'
    decision_making = 'decision_making'
    mentoring = 'mentoring'
    stress_management = 'stress_management'

    CATEGORY_CHOICES = [
        (team_management, 'Team Management'),
        (communication, 'Communication'),
        (leadership, 'Leadership'),
        (problem_solving, 'Problem Solving'),
        (adaptability, 'Adaptability'),
        (time_management, 'Time Management'),
        (conflict_resolution, 'Conflict Resolution'),
        (teamwork, 'Teamwork'),
        (negotiation, 'Negotiation'),
        (creativity, 'Creativity'),
        (decision_making, 'Decision Making'),
        (mentoring, 'Mentoring'),
        (stress_management, 'Stress Management')
    ]

    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)
    category = models.CharField(verbose_name='Category', max_length=25, choices=CATEGORY_CHOICES, default='other')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Resume(models.Model):
    """
    Holds Resume created by the candidate.
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='name', max_length=100, blank=True)
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
    
    technical_skills = models.ManyToManyField(TechnicalSkill, verbose_name='Technical Skills', blank=True)
    soft_skills = models.ManyToManyField(SoftSkill, verbose_name='Soft Skills', blank=True)

    def save(self, *args, **kwargs):
        value = self.unique_id
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


#     skills = models.TextField(verbose_name='Skills')
#     achievements = models.ManyToManyField(Achievement, verbose_name='Achievements')
#     projects = models.ManyToManyField(Project, verbose_name='Projects')
#     additional_sections = models.TextField(verbose_name='Additional Sections', blank=True)
#     work_experience = models.ForeignKey(WorkExperience, verbose_name='Work Experience', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
            value = self.unique_id
            self.slug = slugify(value, allow_unicode=True)
            super().save(*args, **kwargs)

