# Generated by Django 2.2.24 on 2023-07-13 17:16

from django.db import migrations


def transfer_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator():
        Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone)


def delete_owner(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20230713_2015'),
    ]

    operations = [
        migrations.RunPython(transfer_owner, delete_owner),
    ]
