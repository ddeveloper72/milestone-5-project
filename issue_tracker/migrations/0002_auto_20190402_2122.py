# Generated by Django 2.1.7 on 2019-04-02 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='issue_voters',
            new_name='voter',
        ),
    ]
