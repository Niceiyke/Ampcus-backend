# Generated by Django 4.2.7 on 2023-12-12 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0004_comment_loan_alter_loan_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='description',
        ),
    ]
