# Generated by Django 4.2 on 2023-06-18 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_phone_number_booking_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='date_of_shoot',
            new_name='Text',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='end_time',
            new_name='TimeEnd',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='start_time',
            new_name='TimeStart',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='shoot_type',
            new_name='cab',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='number_of_days',
            new_name='passengers',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='pin_code',
            new_name='pinCode',
        ),
    ]
