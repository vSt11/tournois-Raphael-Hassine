# Generated by Django 4.2 on 2023-04-19 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppTournois', '0005_remove_commentaire_match_commentaire_match_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='match_id',
        ),
        migrations.AddField(
            model_name='commentaire',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentaire', to='AppTournois.match'),
        ),
    ]
