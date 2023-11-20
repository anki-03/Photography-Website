# Generated by Django 4.2 on 2023-06-18 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('shoot_type', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('pin_code', models.CharField(max_length=10)),
                ('date_of_shoot', models.DateField()),
                ('number_of_days', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('comments', models.TextField()),
            ],
        ),
    ]
