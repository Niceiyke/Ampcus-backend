# Generated by Django 4.2.7 on 2023-11-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0007_rename_amount_loan_borrowed_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loantype',
            name='name',
            field=models.CharField(choices=[('Jumbo Loan', 'jumbo'), ('Education Loan', 'education')], default='jumbo', max_length=50),
        ),
    ]
