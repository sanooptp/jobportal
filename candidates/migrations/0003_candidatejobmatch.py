# Generated by Django 3.2.3 on 2021-05-31 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
        ('candidates', '0002_alter_candidate_relocate'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateJobMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('accepted', 'Accepted')], default='pending', max_length=50)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
        ),
    ]