# Generated by Django 5.0.6 on 2024-07-15 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0028_message_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='parent',
            new_name='parent_message',
        ),
    ]
