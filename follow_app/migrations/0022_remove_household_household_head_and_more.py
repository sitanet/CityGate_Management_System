# Generated by Django 5.0.6 on 2024-07-13 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0021_household_household_head_householdmember_is_head'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='household_head',
        ),
        migrations.RemoveField(
            model_name='householdmember',
            name='is_head',
        ),
    ]
