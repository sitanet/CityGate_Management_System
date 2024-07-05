# Generated by Django 5.0.6 on 2024-07-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20240619_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Team Lead'), (3, 'Team Member'), (4, 'Pastorate'), (5, 'Facilitator'), (6, 'Student'), (7, 'Career'), (8, 'Business'), (9, 'Service Team'), (10, 'Management Information System')], null=True),
        ),
    ]
