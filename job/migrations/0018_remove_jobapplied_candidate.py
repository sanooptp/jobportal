# Generated by Django 3.2.4 on 2021-06-25 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_remove_job_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplied',
            name='candidate',
        ),
    ]
