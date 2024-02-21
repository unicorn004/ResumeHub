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

    PROGRAMMING_LANGUAGE = 'programming_language'
    FRAMEWORKS = 'frameworks'
    VERSION_CONTROL = 'version_control'
    METHODOLOGIES = 'methodologies'
    DATA_ANALYSIS = 'data_analysis'
    IT_NETWORKING = 'it_networking'
    WEB_DEV_DESIGN = 'web_dev_design'
    AI_ML = 'ai_ml'
    DBMS = 'dbms'
    CLOUD_COMPUTING = 'cloud_computing'

    TEAM_MANAGEMENT = 'team_management'
    COMMUNICATION = 'communication'
    LEADERSHIP = 'leadership'
    PROBLEM_SOLVING = 'problem_solving'
    ADAPTABILITY = 'adaptability'
    TIME_MANAGEMENT = 'time_management'

    CATEGORY_CHOICES = [
        (PROGRAMMING_LANGUAGE, 'Programming Language'),
        (FRAMEWORKS, 'Frameworks and Libraries'),
        (VERSION_CONTROL, 'Version Control Systems'),
        (METHODOLOGIES, 'Development Methodologies'),
        (DATA_ANALYSIS, 'Data Analysis and Analytics'),
        (IT_NETWORKING, 'IT and Networking'),
        (WEB_DEV_DESIGN, 'Web Development and Design'),
        (AI_ML, 'Machine Learning and Artificial Intelligence'),
        (DBMS, 'Database Management'),
        (CLOUD_COMPUTING, 'Cloud Computing'),

        (TEAM_MANAGEMENT, 'Team Management'),
        (COMMUNICATION, 'Communication'),
        (LEADERSHIP, 'Leadership'),
        (PROBLEM_SOLVING, 'Problem Solving'),
        (ADAPTABILITY, 'Adaptability'),
        (TIME_MANAGEMENT, 'Time Management'),
    ]

    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)
    skill_type = models.CharField(verbose_name='Type', max_length=10, choices=SKILL_TYPES)
    category = models.CharField(verbose_name='Category', max_length=20, choices=CATEGORY_CHOICES)
    
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    def save(self, *args, **kwargs):
        value = f'{self.name}'
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
