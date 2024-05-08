# Generated by Django 5.0.2 on 2024-05-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualities', '0009_alter_education_education_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='education_level',
            field=models.CharField(choices=[('primary', 'primary'), ('middle_school', 'middle_school'), ('high_school', 'high_school'), ('higher_secondary', 'higher_secondary'), ('Graduation', 'Graduation'), ('Post Graduation', 'Post Graduation'), ('doctorate', 'doctorate'), ('post_doctorate', 'post_doctorate'), ('diploma', 'diploma'), ('course', 'course'), ('other', 'other')], max_length=50, verbose_name='Level'),
        ),
    ]
