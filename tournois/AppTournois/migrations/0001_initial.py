# Generated by Django 4.2 on 2023-04-18 13:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_equipe', models.CharField(max_length=255)),
                ('nom_entraineur', models.CharField(max_length=255)),
                ('joueurs', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tournoi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tournoi', models.CharField(max_length=255)),
                ('nb_poules', models.IntegerField()),
                ('nb_equipes_poule', models.IntegerField()),
                ('lieu', models.CharField(blank=True, max_length=255, null=True)),
                ('dates', models.DateTimeField(blank=True, null=True)),
                ('liste_equipes', models.ManyToManyField(to='AppTournois.equipe')),
            ],
        ),
        migrations.CreateModel(
            name='Poule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_poule', models.IntegerField()),
                ('equipes', models.ManyToManyField(to='AppTournois.equipe')),
                ('tournoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTournois.tournoi')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField()),
                ('lieu', models.CharField(max_length=255)),
                ('score_equipe1', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('score_equipe2', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('commentaire', models.CharField(blank=True, max_length=255, null=True)),
                ('equipe1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipe1', to='AppTournois.equipe')),
                ('equipe2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipe2', to='AppTournois.equipe')),
                ('numero_poule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppTournois.poule')),
            ],
        ),
        migrations.CreateModel(
            name='commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.CharField(blank=True, max_length=200, null=True)),
                ('date_heure', models.DateTimeField(auto_now_add=True)),
                ('contenu', models.TextField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
