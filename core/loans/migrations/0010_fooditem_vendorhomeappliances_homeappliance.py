# Generated by Django 4.2.7 on 2023-11-28 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0009_alter_loantype_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=240, null=True)),
                ('price', models.PositiveIntegerField()),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('starting_date', models.DateTimeField()),
                ('closing_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VendorHomeAppliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='HomeAppliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=240, null=True)),
                ('price', models.PositiveIntegerField()),
                ('starting_date', models.DateTimeField()),
                ('closing_date', models.DateTimeField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.vendorhomeappliances')),
            ],
        ),
    ]