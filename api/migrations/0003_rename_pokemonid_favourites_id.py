# Generated by Django 5.1 on 2024-08-21 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_favourites_abilities_favourites_forms_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favourites',
            old_name='pokemonId',
            new_name='id',
        ),
    ]
