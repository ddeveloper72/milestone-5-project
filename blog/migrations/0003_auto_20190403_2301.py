# Generated by Django 2.1.7 on 2019-04-03 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_userseenposts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userseenposts',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='seen_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
