# Generated by Django 2.2.24 on 2023-07-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20230713_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='owner',
        ),
        migrations.AddField(
            model_name='owner',
            name='name',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='ФИО владельца:'),
        ),
    ]