# Generated by Django 4.0.4 on 2022-10-14 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_alter_pokemon_hp_alter_pokemon_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='name_ar',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='name_fr',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='name_jp',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
