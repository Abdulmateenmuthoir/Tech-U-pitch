# Generated by Django 4.2.16 on 2025-03-19 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='country',
            new_name='university',
        ),
    ]
