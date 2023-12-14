# Generated by Django 4.2.7 on 2023-12-12 21:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0006_alter_comment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_commented',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]