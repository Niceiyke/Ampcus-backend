# Generated by Django 4.2.7 on 2023-12-12 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_rename_is_tresurer_approved_loan_is_treasurer_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='loan',
            field=models.ForeignKey(default='bdc1773d-879f-4548-8092-8645df8ea035', on_delete=django.db.models.deletion.CASCADE, to='loans.loan'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loan',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='loanComment', to='loans.comment'),
        ),
    ]
