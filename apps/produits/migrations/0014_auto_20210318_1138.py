# Generated by Django 3.1.7 on 2021-03-18 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0013_auto_20210318_1138'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='produit',
            unique_together={('nature_produit', 'nom_produit', 'date_donation')},
        ),
    ]