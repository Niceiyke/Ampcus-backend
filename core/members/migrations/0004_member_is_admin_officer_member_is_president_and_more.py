# Generated by Django 4.2.7 on 2023-12-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_admin_officer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_president',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_treasurer',
            field=models.BooleanField(default=False),
        ),
    ]
