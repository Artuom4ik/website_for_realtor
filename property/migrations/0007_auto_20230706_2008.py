# Generated by Django 2.2.24 on 2023-07-06 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20230706_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.Flat', verbose_name='Квартира, на которую пожаловались:'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался:'),
        ),
    ]
