# Generated by Django 5.0.6 on 2024-07-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_system', '0006_asset_asset_class_alter_asset_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='unit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
