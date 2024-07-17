# Generated by Django 5.0.6 on 2024-07-16 08:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0029_rename_parent_message_parent_message'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='past_username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='past_households', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='household',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_households', to=settings.AUTH_USER_MODEL),
        ),
    ]
