# Generated by Django 3.2.3 on 2021-06-09 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_jobapplied_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='jobapplied',
            name='username',
        ),
    ]