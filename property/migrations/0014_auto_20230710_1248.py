# Generated by Django 2.2.24 on 2023-07-10 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner_flat',
            new_name='owner',
        ),
    ]