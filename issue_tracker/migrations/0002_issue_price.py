# Generated by Django 2.1.7 on 2019-04-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='price',
            field=models.DecimalField(decimal_places=2, default=80.0, max_digits=6),
        ),
    ]
