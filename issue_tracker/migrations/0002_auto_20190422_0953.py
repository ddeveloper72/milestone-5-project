# Generated by Django 2.1.7 on 2019-04-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('In Progress', 'In Progress'), ('Complete', 'Complete')], default='To do', max_length=12),
        ),
    ]
