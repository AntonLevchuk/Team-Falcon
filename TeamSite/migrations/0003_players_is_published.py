# Generated by Django 3.2 on 2021-04-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamSite', '0002_rename_title_players_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
