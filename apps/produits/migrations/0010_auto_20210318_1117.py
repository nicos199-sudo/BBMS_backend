# Generated by Django 3.1.7 on 2021-03-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0009_auto_20210318_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date_donation',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='date_donation',
            field=models.DateTimeField(),
        ),
    ]
