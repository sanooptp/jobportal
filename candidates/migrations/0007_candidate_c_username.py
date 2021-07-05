# Generated by Django 3.2.3 on 2021-06-09 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidates', '0006_remove_candidate_c_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='c_username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Username'),
            preserve_default=False,
        ),
    ]