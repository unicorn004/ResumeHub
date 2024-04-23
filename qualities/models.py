from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User

class Education(models.Model):
    """
    Holds the candidate's educational qualifications
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE)
    
    # Education Level Choices
    primary = 'primary'
    middle_school = 'middle_school'
    high_school = 'high_school'
    higher_secondary =  'higher_secondary'
    graduation = 'graduation'
    post_graduation = 'post_graduation'
    doctorate = 'doctorate'
    post_doctorate = 'post_doctorate'
    diploma = 'diploma'
    course = 'course'
    other = 'other'

    EDUCATION_LEVEL_CHOICES = [
        (primary, 'primary'),
        (middle_school, 'middle_school'),
        (high_school, 'high_school'),
        (higher_secondary,  'higher_secondary'),
        (graduation, 'graduation'),
        (post_graduation, 'post_graduation'),
        (doctorate, 'doctorate'),
        (post_doctorate, 'post_doctorate'),
        (diploma, 'diploma'),
        (course, 'course'),
        (other, 'other'),
    ]

    education_level = models.CharField(verbose_name='Level', max_length=20, choices=EDUCATION_LEVEL_CHOICES)
    institute = models.CharField(verbose_name='Institute', max_length=150,)
    additional_info = models.TextField(verbose_name='Additional Info', null=True, blank=True)
    date_of_passing = models.DateTimeField(verbose_name='Date of Passing', null=True)
    pursuing = models.BooleanField(verbose_name='Pursuing', default=False)

    def __str__(self):
        return f'{self.education_level}-{self.institute}'


class Hobby(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)

    def save(self, *args, **kwargs):
        value = f'{self.name}'
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
        

class TechnicalSkill(models.Model):
    """
    Model to represent technical skills.
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, related_name='technical_skills')
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)

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
    other = 'other'

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

    skill_type = 'technical'

    category = models.CharField(verbose_name='Category', max_length=25, choices=CATEGORY_CHOICES, default=other)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - Technical Skill'

class SoftSkill(models.Model):
    """
    Model to represent soft skills.
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, related_name='soft_skills')
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)

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

    skill_type = 'soft'

    category = models.CharField(verbose_name='Category', max_length=25, choices=CATEGORY_CHOICES)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - Soft Skill'
