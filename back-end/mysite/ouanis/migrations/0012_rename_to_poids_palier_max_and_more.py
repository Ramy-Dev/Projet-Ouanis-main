# Generated by Django 5.0.2 on 2024-06-14 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ouanis', '0011_demandeannonce_prix_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='palier',
            old_name='to_poids',
            new_name='max',
        ),
        migrations.RenameField(
            model_name='palier',
            old_name='from_poids',
            new_name='min',
        ),
        migrations.RenameField(
            model_name='palier',
            old_name='prix',
            new_name='price',
        ),
    ]
