# Generated by Django 2.2.24 on 2023-07-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230710_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flat',
            field=models.ManyToManyField(related_name='flat_owner', to='property.Flat', verbose_name='Квартиры в собсвенности:'),
        ),
    ]
