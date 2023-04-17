# Generated by Django 2.2.12 on 2023-04-17 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppTournois', '0004_auto_20230417_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.CharField(max_length=200)),
                ('date_heure', models.DateTimeField(auto_now_add=True)),
                ('contenu', models.TextField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]