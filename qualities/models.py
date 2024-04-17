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
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='Slug', null=True, blank=True)

    def save(self, *args, **kwargs):
        value = f'{self.name}'
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

# class Skill(models.Model):
#     technical = 'technical'
#     soft = 'soft'
#     skill_types = [
#         (technical, 'Technical Skill'),
#         (soft, 'Soft Skill')
#     ]

#     programming_language = 'programming_language'
#     frameworks = 'frameworks'
#     version_control = 'version_control'
#     methodologies = 'methodologies'
#     data_analysis = 'data_analysis'
#     it_networking = 'it_networking'
#     web_dev_design = 'web_dev_design'
#     ai_ml = 'ai_ml'
#     dbms = 'dbms'
#     cloud_computing = 'cloud_computing'

#     team_management = 'team_management'
#     communication = 'communication'
#     leadership = 'leadership'
#     problem_solving = 'problem_solving'
#     adaptability = 'adaptability'
#     time_management = 'time_management'
#     conflict_resolution = 'conflict_resolution'
#     teamwork = 'teamwork'
#     negotiation = 'negotiation'
#     creativity = 'creativity'
#     decision_making = 'decision_making'
#     mentoring = 'mentoring'
#     stress_management = 'stress_management'

#     category_choices = [
#         (programming_language, 'Programming Language'),
#         (frameworks, 'Frameworks and Libraries'),
#         (version_control, 'Version Control Systems'),
#         (methodologies, 'Development Methodologies'),
#         (data_analysis, 'Data Analysis and Analytics'),
#         (it_networking, 'IT and Networking'),
#         (web_dev_design, 'Web Development and Design'),
#         (ai_ml, 'Machine Learning and Artificial Intelligence'),
#         (dbms, 'Database Management'),
#         (cloud_computing, 'Cloud Computing'),

#         (team_management, 'Team Management'),
#         (communication, 'Communication'),
#         (leadership, 'Leadership'),
#         (problem_solving, 'Problem Solving'),
#         (adaptability, 'Adaptability'),
#         (time_management, 'Time Management'),
#         (conflict_resolution, 'Conflict Resolution'),
#         (teamwork, 'Teamwork'),
#         (negotiation, 'Negotiation'),
#         (creativity, 'Creativity'),
#         (decision_making, 'Decision Making'),
#         (mentoring, 'Mentoring'),
#         (stress_management, 'Stress Management'),
        
#         ('python', 'Python'),
#         ('java', 'Java'),
#         ('javascript', 'JavaScript'),
#         ('c++', 'C++'),
#         ('c#', 'C#'),
#         ('php', 'PHP'),
#         ('ruby', 'Ruby'),
#         ('go', 'Go'),
#         ('rust', 'Rust'),
#         ('kotlin', 'Kotlin'),
#         ('html/css', 'HTML/CSS'),
#         ('sql', 'SQL'),
#         ('r', 'R Programming Language'),
#         ('matlab', 'MATLAB'),
#         ('assembly', 'Assembly Language')
#     ]

#     unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     name = models.CharField(verbose_name='Name', max_length=100, unique=True)
#     slug = models.SlugField(verbose_name='Slug', null=True, blank=True)
#     skill_type = models.CharField(verbose_name='Type', max_length=10, choices=skill_types)
#     category = models.CharField(verbose_name='Category', max_length=25, choices=category_choices)
    
#     description = models.TextField(verbose_name='Description', blank=True, null=True)



# # Testimonial
# class Testimonial(models.Model):
#     unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, blank=True, null=True)
#     source = models.CharField(verbose_name='Source', max_length=255)
#     content = models.TextField(verbose_name='Content')
#     date = models.DateField(verbose_name='Date')




# # Work Experience
# class WorkExperience(models.Model):
#     candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, blank=True, null=True)
#     unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     position = models.CharField(verbose_name='Position', max_length=255)
#     company = models.CharField(verbose_name='Company/Organization', max_length=255)
#     location = models.CharField(verbose_name='Location', max_length=255)
#     employment_duration = models.CharField(verbose_name='Employment Duration', max_length=255)
#     responsibilities = models.TextField(verbose_name='Responsibilities')



# # Project
# class Project(models.Model):
#     unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, blank=True, null=True)
#     name = models.CharField(verbose_name='Project Name', max_length=255)
#     description = models.TextField(verbose_name='Description', blank=True)
#     start_date = models.DateField(verbose_name='Start Date', blank=True, null=True)
#     end_date = models.DateField(verbose_name='End Date', blank=True, null=True)


# # Achievement
# class Achievement(models.Model):
#     name = models.CharField(verbose_name='Achievement Name', max_length=255)
#     candidate = models.ForeignKey(User, verbose_name='Candidate', on_delete=models.CASCADE, blank=True, null=True)
#     description = models.TextField(verbose_name='Description', blank=True)
#     date_achieved = models.DateField(verbose_name='Date Achieved', blank=True, null=True)
#     related_project = models.ForeignKey(Project, verbose_name='Related Project', on_delete=models.CASCADE, blank=True, null=True)
#     certificate_file = models.FileField(verbose_name='Certificate File', upload_to='certificates/', blank=True, null=True)
