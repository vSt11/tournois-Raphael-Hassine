# Generated by Django 4.2 on 2023-04-18 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppTournois', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='AppTournois.match'),
        ),
    ]
