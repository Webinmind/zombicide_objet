# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'1b', max_length=255)),
                ('ref', models.CharField(default=b'1b', max_length=255)),
                ('color', models.CharField(choices=[(b'red', b'Rouge'), (b'blue', b'Bleu'), (b'green', b'Vert')], max_length=255)),
                ('top', models.IntegerField(default=0)),
                ('left', models.IntegerField(default=0)),
                ('angle', models.IntegerField(default=0)),
                ('dropped', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'1b', max_length=255)),
                ('ref', models.CharField(default=b'1b', max_length=255)),
                ('color', models.CharField(choices=[(b'red', b'Rouge'), (b'blue', b'Bleu'), (b'green', b'Vert')], max_length=255)),
                ('state', models.CharField(choices=[(b'open', b'Ouverte'), (b'close', 'Ferm\xe9e')], max_length=255)),
                ('top', models.IntegerField(default=0)),
                ('left', models.IntegerField(default=0)),
                ('angle', models.IntegerField(default=0)),
                ('dropped', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Exit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'noise', max_length=255)),
                ('ref', models.CharField(default=b'noise', max_length=255)),
                ('color', models.CharField(choices=[(b'red', b'Rouge'), (b'blue', b'Bleu'), (b'green', b'Vert')], max_length=255)),
                ('type', models.CharField(choices=[(b'exit', b'Sortie'), (b'noise', b'Bruit')], default=b'exit', max_length=255, verbose_name=b'Sortie')),
                ('top', models.IntegerField(default=0)),
                ('left', models.IntegerField(default=0)),
                ('angle', models.IntegerField(default=0)),
                ('dropped', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=255)),
                ('number', models.IntegerField(blank=True, default=666, null=True)),
                ('active', models.BooleanField(default=True)),
                ('resume', models.TextField(blank=True, default=b'')),
                ('objectives', models.TextField(blank=True, default=b'')),
                ('special_rules', models.TextField(blank=True, default=b'')),
                ('difficulty', models.CharField(default=b'Easy', max_length=255)),
                ('nb_of_player', models.CharField(default=b'6', max_length=255)),
                ('mission_time', models.CharField(default=b'', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ModalCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'car_police', max_length=255, verbose_name=b'Nom')),
                ('season', models.CharField(choices=[(b'season_one', b'Season One'), (b'angry_neighbors', b'Angry Neighbors'), (b'prison_outbreak', b'Prison Outbreak'), (b'rue_morgue', b'Rue Morgue'), (b'toxic_city_mall', b'Toxic City Mall'), (b'silhouette_pack', b'Silhouette Pack')], max_length=255, verbose_name=b'Saison')),
                ('type', models.CharField(choices=[(b'police', b'Bagnole de Flics'), (b'pimp', b'Pimpmobile')], max_length=255, verbose_name=b'Type de bagnole')),
                ('picture', models.CharField(max_length=500, verbose_name=b'Image')),
            ],
        ),
        migrations.CreateModel(
            name='ModalDoor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'door_blue', max_length=255, verbose_name=b'Nom')),
                ('season', models.CharField(choices=[(b'season_one', b'Season One'), (b'angry_neighbors', b'Angry Neighbors'), (b'prison_outbreak', b'Prison Outbreak'), (b'rue_morgue', b'Rue Morgue'), (b'toxic_city_mall', b'Toxic City Mall'), (b'silhouette_pack', b'Silhouette Pack')], max_length=255, verbose_name=b'Saison')),
                ('picture', models.CharField(max_length=500, verbose_name=b'Image')),
                ('color', models.CharField(choices=[(b'red', b'Rouge'), (b'blue', b'Bleu'), (b'green', b'Vert')], max_length=255, verbose_name=b'Couleur')),
                ('state', models.CharField(choices=[(b'open', b'Ouverte'), (b'close', 'Ferm\xe9e')], max_length=255, verbose_name='\xc9tat')),
            ],
        ),
        migrations.CreateModel(
            name='ModalExit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'car_police', max_length=255, verbose_name=b'Nom')),
                ('season', models.CharField(choices=[(b'season_one', b'Season One'), (b'angry_neighbors', b'Angry Neighbors'), (b'prison_outbreak', b'Prison Outbreak'), (b'rue_morgue', b'Rue Morgue'), (b'toxic_city_mall', b'Toxic City Mall'), (b'silhouette_pack', b'Silhouette Pack')], max_length=255, verbose_name=b'Saison')),
                ('type', models.CharField(choices=[(b'exit', b'Sortie'), (b'noise', b'Bruit')], max_length=255, verbose_name=b'Type de bagnole')),
                ('picture', models.CharField(max_length=500, verbose_name=b'Image')),
            ],
        ),
        migrations.CreateModel(
            name='ModalNoise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'car_police', max_length=255, verbose_name=b'Nom')),
                ('season', models.CharField(choices=[(b'season_one', b'Season One'), (b'angry_neighbors', b'Angry Neighbors'), (b'prison_outbreak', b'Prison Outbreak'), (b'rue_morgue', b'Rue Morgue'), (b'toxic_city_mall', b'Toxic City Mall'), (b'silhouette_pack', b'Silhouette Pack')], max_length=255, verbose_name=b'Saison')),
                ('type', models.CharField(choices=[(b'exit', b'Sortie'), (b'noise', b'Bruit')], max_length=255, verbose_name=b'Jeton de bruit')),
                ('picture', models.CharField(max_length=500, verbose_name=b'Image')),
            ],
        ),
        migrations.CreateModel(
            name='ModalObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'objective_blue', max_length=255, verbose_name=b'Nom')),
                ('season', models.CharField(choices=[(b'season_one', b'Season One'), (b'angry_neighbors', b'Angry Neighbors'), (b'prison_outbreak', b'Prison Outbreak'), (b'rue_morgue', b'Rue Morgue'), (b'toxic_city_mall', b'Toxic City Mall'), (b'silhouette_pack', b'Silhouette Pack')], max_length=255, verbose_name=b'Saison')),
                ('color', models.CharField(choices=[(b'red', b'Rouge'), (b'blue', b'Bleu'), (b'green', b'Vert')], max_length=255, verbose_name=b'Couleur')),
                ('picture', models.CharField(max_length=500, verbose_name=b'Image')),
            ],
        ),
        migrations.CreateModel(
            name='ModalSpawn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'spawn_blue', max_length=255, verbose_name=b'Nom')),
                ('season', models.CharField(choices=[(b'season_one', b'Season One'), (b'angry_neighbors', b'Angry Neighbors'), (b'prison_outbreak', b'Prison Outbreak'), (b'rue_morgue', b'Rue Morgue'), (b'toxic_city_mall', b'Toxic City Mall'), (b'silhouette_pack', b'Silhouette Pack')], max_length=255, verbose_name=b'Saison')),
                ('color', models.CharField(choices=[(b'red', b'Rouge'), (b'blue', b'Bleu'), (b'green', b'Vert')], max_length=255, verbose_name=b'Couleur')),
                ('picture', models.CharField(max_length=500, verbose_name=b'Image')),
            ],
        ),
        migrations.CreateModel(
            name='ModalTile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'1b', max_length=255, verbose_name=b'Nom')),
                ('season', models.CharField(choices=[(b'season_one', b'Season One'), (b'angry_neighbors', b'Angry Neighbors'), (b'prison_outbreak', b'Prison Outbreak'), (b'rue_morgue', b'Rue Morgue'), (b'toxic_city_mall', b'Toxic City Mall'), (b'silhouette_pack', b'Silhouette Pack')], max_length=255, verbose_name=b'Saison')),
                ('picture', models.CharField(max_length=500, verbose_name=b'Image')),
                ('parent', models.CharField(default=b'A', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Noise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'noise', max_length=255)),
                ('ref', models.CharField(default=b'noise', max_length=255)),
                ('color', models.CharField(choices=[(b'red', b'Rouge'), (b'blue', b'Bleu'), (b'green', b'Vert')], max_length=255)),
                ('type', models.CharField(choices=[(b'exit', b'Sortie'), (b'noise', b'Bruit')], default=b'noise', max_length=255, verbose_name=b'Jeton de bruit')),
                ('top', models.IntegerField(default=0)),
                ('left', models.IntegerField(default=0)),
                ('angle', models.IntegerField(default=0)),
                ('dropped', models.BooleanField(default=False)),
                ('mission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='editeur.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'red', max_length=255)),
                ('ref', models.CharField(default=b'red', max_length=255)),
                ('color', models.CharField(choices=[(b'red', b'Rouge'), (b'blue', b'Bleu'), (b'green', b'Vert')], max_length=255)),
                ('top', models.FloatField(default=0)),
                ('left', models.FloatField(default=0)),
                ('angle', models.IntegerField(default=0)),
                ('dropped', models.BooleanField(default=False)),
                ('mission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='editeur.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='Spawn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'red', max_length=255)),
                ('ref', models.CharField(default=b'red', max_length=255)),
                ('color', models.CharField(choices=[(b'red', b'Rouge'), (b'blue', b'Bleu'), (b'green', b'Vert')], max_length=255)),
                ('top', models.FloatField(default=0)),
                ('left', models.FloatField(default=0)),
                ('angle', models.IntegerField(default=0)),
                ('dropped', models.BooleanField(default=False)),
                ('mission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='editeur.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'1b', max_length=255)),
                ('top', models.FloatField(default=0)),
                ('left', models.FloatField(default=0)),
                ('angle', models.IntegerField(default=0)),
                ('dropped', models.BooleanField(default=False)),
                ('parent', models.CharField(default=b'1b', max_length=255)),
                ('mission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='editeur.Mission')),
            ],
        ),
        migrations.AddField(
            model_name='exit',
            name='mission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='editeur.Mission'),
        ),
        migrations.AddField(
            model_name='door',
            name='mission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='editeur.Mission'),
        ),
        migrations.AddField(
            model_name='car',
            name='mission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='editeur.Mission'),
        ),
    ]
