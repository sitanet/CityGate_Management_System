# Generated by Django 5.0.6 on 2024-07-13 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0019_remove_householdmember_name_householdmember_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='username',
        ),
        migrations.AddField(
            model_name='household',
            name='members',
            field=models.ManyToManyField(through='follow_app.HouseholdMember', to='follow_app.member'),
        ),
        migrations.AlterField(
            model_name='householdmember',
            name='household',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.household'),
        ),
        migrations.AlterField(
            model_name='householdmember',
            name='position',
            field=models.CharField(max_length=100),
        ),
    ]