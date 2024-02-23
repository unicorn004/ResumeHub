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
    technical = 'technical'
    soft = 'soft'
    skill_types = [
        (technical, 'Technical Skill'),
        (soft, 'Soft Skill')
    ]

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

    category_choices = [
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
        (stress_management, 'Stress Management'),
        
        ('python', 'Python'),
        ('java', 'Java'),
        ('javascript', 'JavaScript'),
        ('c++', 'C++'),
        ('c#', 'C#'),
        ('php', 'PHP'),
        ('ruby', 'Ruby'),
        ('go', 'Go'),
        ('rust', 'Rust'),
        ('kotlin', 'Kotlin'),
        ('html/css', 'HTML/CSS'),
        ('sql', 'SQL'),
        ('r', 'R Programming Language'),
        ('matlab', 'MATLAB'),
        ('assembly', 'Assembly Language')
    ]

    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)
    skill_type = models.CharField(verbose_name='Type', max_length=10, choices=skill_types)
    category = models.CharField(verbose_name='Category', max_length=25, choices=category_choices)
    
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    def save(self, *args, **kwargs):
        value = f'{self.name}'
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
