# Generated by Django 4.0.1 on 2023-05-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('message', models.TextField(max_length=30)),
            ],
        ),
    ]
