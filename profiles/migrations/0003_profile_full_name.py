# Generated by Django 5.0.2 on 2024-04-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_facebook_url_profile_instagram_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
