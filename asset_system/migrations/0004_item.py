# Generated by Django 5.0.6 on 2024-06-30 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_system', '0003_alter_asset_assigned_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
