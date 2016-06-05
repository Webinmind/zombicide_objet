# -*- coding: utf-8 -*-
from django.db import models
from django import forms

TILE_FOLDER = (
    ('season_one'      , 'imgs/tiles/G-Zombicrefe/tiles/'),
    ('angry_neighbors' , 'imgs/tiles/G-Zombicrefe-AN/tiles/'),
    ('prison_outbreak' , 'imgs/tiles/G-Zombicrefe-PO/tiles/'),
    ('rue_morgue'      , 'imgs/tiles/G-Zombicrefe-RM/tiles/'),
    ('toxic_city_mall' , 'imgs/tiles/G-Zombicrefe-TCM/tiles/'),
    ('silhouette_pack' , 'imgs/tiles/G-Zombicrefe-Z/tiles/')
)

color = (
    ('red', 'Rouge'),
    ('blue', 'Bleu'),
    ('green', 'Vert'),
)

DOOR_STATE = (
    ('open', 'Ouverte'),
    ('close', u'Fermée'),
)

CAR_TYPE = (
    ('police', 'Bagnole de Flics'),
    ('pimp'  , 'Pimpmobile'),
)

GENERAL_type = (
    ('exit', 'Sortie'),
    ('noise', 'Bruit'),
)

SEASON_CHOICE = (
    ('season_one'      , 'Season One'),
    ('angry_neighbors' , 'Angry Neighbors'),
    ('prison_outbreak' , 'Prison Outbreak'),
    ('rue_morgue'      , 'Rue Morgue'),
    ('toxic_city_mall' , 'Toxic City Mall'),
    ('silhouette_pack' , 'Silhouette Pack')
)

# MISSION
class Mission(models.Model):
    name          = models.CharField(max_length=255, default='', blank=False, null=False)
    number        = models.IntegerField(default=666, blank=True, null=True)
    active        = models.BooleanField(default=True)
    resume        = models.TextField(blank=True,null=False, default='')
    objectives    = models.TextField(blank=True,null=False, default='')
    special_rules = models.TextField(blank=True,null=False, default='')
    difficulty    = models.CharField(max_length=255, default='Easy', blank=False, null=False)
    nb_of_player  = models.CharField(max_length=255, default='6', blank=False, null=False)
    mission_time  = models.CharField(max_length=255, default='', blank=False, null=False)

    def __unicode__(self):
        return u'%s-%s' % (self.pk, self.name)

    def get_absolute_url(self):
        return "/mission/%i/" % self.id

# TILES
class Tile(models.Model):
    name   = models.CharField(max_length=255, blank=False, null=False, default='1b')
    mission     = models.ForeignKey('Mission', blank=True, null=True)
    top         = models.FloatField(default=0, blank=False, null=False)
    left        = models.FloatField(default=0, blank=False, null=False)
    angle       = models.IntegerField(default=0, blank=False, null=False)
    dropped     = models.BooleanField(default=False)
    parent      = models.CharField(max_length=255, blank=False, null=False, default='1b')

    def __unicode__(self):
        return u'%s' % (self.name)

# OBJECTIVES
class Objective(models.Model):
    name  = models.CharField(max_length=255, blank=False, null=False, default='red')
    ref    = models.CharField(max_length=255, blank=False, null=False, default='red')
    color = models.CharField(max_length=255, blank=False, null=False, choices=color)
    top         = models.FloatField(default=0, blank=False, null=False)
    left        = models.FloatField(default=0, blank=False, null=False)
    angle       = models.IntegerField(default=0, blank=False, null=False)
    mission     = models.ForeignKey('Mission', blank=True, null=True)
    dropped     = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.color)

# SPAWNS
class Spawn(models.Model):
    name  = models.CharField(max_length=255, blank=False, null=False, default='red')
    ref    = models.CharField(max_length=255, blank=False, null=False, default='red')
    color = models.CharField(max_length=255, blank=False, null=False, choices=color)
    top         = models.FloatField(default=0, blank=False, null=False)
    left        = models.FloatField(default=0, blank=False, null=False)
    angle       = models.IntegerField(default=0, blank=False, null=False)
    mission     = models.ForeignKey('Mission', blank=True, null=True)
    dropped     = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.color)

# DOORS
class Door(models.Model):
    name  = models.CharField(max_length=255, blank=False, null=False, default='1b')
    ref    = models.CharField(max_length=255, blank=False, null=False, default='1b')
    color = models.CharField(max_length=255, blank=False, null=False, choices=color)
    state       = models.CharField(max_length=255, blank=False, null=False, choices=DOOR_STATE)
    top         = models.IntegerField(default=0, blank=False, null=False)
    left        = models.IntegerField(default=0, blank=False, null=False)
    angle       = models.IntegerField(default=0, blank=False, null=False)
    mission     = models.ForeignKey('Mission', blank=True, null=True)
    dropped     = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s - %s - %s' % (self.name, self.color, self.state)

# CARS
class Car(models.Model):
    name  = models.CharField(max_length=255, blank=False, null=False, default='1b')
    ref    = models.CharField(max_length=255, blank=False, null=False, default='1b')
    color = models.CharField(max_length=255, blank=False, null=False, choices=color)
    top         = models.IntegerField(default=0, blank=False, null=False)
    left        = models.IntegerField(default=0, blank=False, null=False)
    angle       = models.IntegerField(default=0, blank=False, null=False)
    mission     = models.ForeignKey('Mission', blank=True, null=True)
    dropped     = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.color)

# TOKEN NOISE
class Noise(models.Model):
    name  = models.CharField(max_length=255, blank=False, null=False, default='noise')
    ref    = models.CharField(max_length=255, blank=False, null=False, default='noise')
    color = models.CharField(max_length=255, blank=False, null=False, choices=color)
    type  = models.CharField(max_length=255, blank=False, null=False, choices=GENERAL_type, default='noise', verbose_name="Jeton de bruit")
    top         = models.IntegerField(default=0, blank=False, null=False)
    left        = models.IntegerField(default=0, blank=False, null=False)
    angle       = models.IntegerField(default=0, blank=False, null=False)
    mission     = models.ForeignKey('Mission', blank=True, null=True)
    dropped     = models.BooleanField(default=False)

# TOKEN EXIT
class Exit(models.Model):
    name  = models.CharField(max_length=255, blank=False, null=False, default='noise')
    ref    = models.CharField(max_length=255, blank=False, null=False, default='noise')
    color = models.CharField(max_length=255, blank=False, null=False, choices=color)
    type  = models.CharField(max_length=255, blank=False, null=False, choices=GENERAL_type, default='exit', verbose_name="Sortie")
    top         = models.IntegerField(default=0, blank=False, null=False)
    left        = models.IntegerField(default=0, blank=False, null=False)
    angle       = models.IntegerField(default=0, blank=False, null=False)
    mission     = models.ForeignKey('Mission', blank=True, null=True)
    dropped     = models.BooleanField(default=False)

# MODAL
class ModalTile(models.Model):
    name   = models.CharField(max_length=255, blank=False, null=False, default='1b', verbose_name="Nom")
    season      = models.CharField(max_length=255, blank=False, null=False, choices=SEASON_CHOICE, verbose_name="Saison")
    picture     = models.CharField(max_length=500, blank=False, null=False, verbose_name="Image")
    parent      = models.CharField(max_length=255, blank=False, null=False, default='A')

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.season, self.parent)

# OBJECTIVES
class ModalObjective(models.Model):
    name   = models.CharField(max_length=255, blank=False, null=False, default='objective_blue', verbose_name="Nom")
    season      = models.CharField(max_length=255, blank=False, null=False, choices=SEASON_CHOICE, verbose_name="Saison")
    color = models.CharField(max_length=255, blank=False, null=False, choices=color, verbose_name="Couleur")
    picture     = models.CharField(max_length=500, blank=False, null=False, verbose_name="Image")

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.season, self.color)

# SPAWN
class ModalSpawn(models.Model):
    name   = models.CharField(max_length=255, blank=False, null=False, default='spawn_blue', verbose_name="Nom")
    season      = models.CharField(max_length=255, blank=False, null=False, choices=SEASON_CHOICE, verbose_name="Saison")
    color = models.CharField(max_length=255, blank=False, null=False, choices=color, verbose_name="Couleur")
    picture     = models.CharField(max_length=500, blank=False, null=False, verbose_name="Image")

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.season, self.color)

# DOOR
class ModalDoor(models.Model):
    name   = models.CharField(max_length=255, blank=False, null=False, default='door_blue', verbose_name="Nom")
    season      = models.CharField(max_length=255, blank=False, null=False, choices=SEASON_CHOICE, verbose_name="Saison")
    picture     = models.CharField(max_length=500, blank=False, null=False, verbose_name="Image")
    color = models.CharField(max_length=255, blank=False, null=False, choices=color, verbose_name="Couleur")
    state       = models.CharField(max_length=255, blank=False, null=False, choices=DOOR_STATE, verbose_name=u"État")

    def __unicode__(self):
        return u'%s %s %s %s' % (self.name, self.season, self.color, self.state)

# CAR
class ModalCar(models.Model):
    name   = models.CharField(max_length=255, blank=False, null=False, default='car_police', verbose_name="Nom")
    season      = models.CharField(max_length=255, blank=False, null=False, choices=SEASON_CHOICE, verbose_name="Saison")
    type  = models.CharField(max_length=255, blank=False, null=False, choices=CAR_TYPE, verbose_name="Type de bagnole")
    picture     = models.CharField(max_length=500, blank=False, null=False, verbose_name="Image")

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.season, self.type)

# TOKEN NOISE
class ModalNoise(models.Model):
    name   = models.CharField(max_length=255, blank=False, null=False, default='car_police', verbose_name="Nom")
    season      = models.CharField(max_length=255, blank=False, null=False, choices=SEASON_CHOICE, verbose_name="Saison")
    type  = models.CharField(max_length=255, blank=False, null=False, choices=GENERAL_type, verbose_name="Jeton de bruit")
    picture     = models.CharField(max_length=500, blank=False, null=False, verbose_name="Image")

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.season, self.type)

# TOKEN EXIT
class ModalExit(models.Model):
    name   = models.CharField(max_length=255, blank=False, null=False, default='car_police', verbose_name="Nom")
    season      = models.CharField(max_length=255, blank=False, null=False, choices=SEASON_CHOICE, verbose_name="Saison")
    type  = models.CharField(max_length=255, blank=False, null=False, choices=GENERAL_type, verbose_name="Type de bagnole")
    picture     = models.CharField(max_length=500, blank=False, null=False, verbose_name="Image")

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.season, self.type)