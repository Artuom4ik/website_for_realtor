# Generated by Django 2.2.24 on 2023-07-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20230713_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собсвенности:'),
        ),
    ]
