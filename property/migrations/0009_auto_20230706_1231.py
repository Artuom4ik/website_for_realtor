# Generated by Django 2.2.24 on 2023-07-06 09:31
import phonenumbers
from django.db import migrations


def normalize_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if phonenumbers.is_valid_number(phonenumbers.parse(flat.owners_phonenumber, "RU")):
            flat.owner_pure_phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20230706_1230'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumber),
    ]