# Generated by Django 2.1.7 on 2019-04-07 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='category',
            field=models.CharField(choices=[('BUG', 'BUG'), ('FEATURE', 'FEATURE')], default='BUG', max_length=10),
        ),
    ]
