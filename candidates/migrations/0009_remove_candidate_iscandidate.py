# Generated by Django 3.2.4 on 2021-06-16 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0008_candidate_iscandidate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='iscandidate',
        ),
    ]
