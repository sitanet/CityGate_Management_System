# Generated by Django 3.2.20 on 2024-06-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Team Lead'), (3, 'Team Member'), (4, 'Pastorate'), (5, 'Facilitator'), (6, 'Student'), (7, 'Career'), (8, 'Business'), (9, 'Service Team')], null=True),
        ),
    ]
