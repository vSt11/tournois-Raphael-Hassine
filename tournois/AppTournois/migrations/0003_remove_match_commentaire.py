# Generated by Django 4.2 on 2023-04-18 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTournois', '0002_alter_commentaire_match'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='commentaire',
        ),
    ]