# Generated by Django 3.2 on 2021-04-27 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TeamSite', '0005_tournaments_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournaments',
            options={'ordering': ['-created_at'], 'verbose_name': 'Турнир', 'verbose_name_plural': 'Турниры'},
        ),
    ]
