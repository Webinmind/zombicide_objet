# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

# Register your models here.
class MissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','active',)
    list_filter = ('name','active',)

class TileAdmin(admin.ModelAdmin):
    list_display = ('name', 'top', 'left', 'angle', 'mission', 'dropped',)
    list_filter  = ('name', 'top', 'left', 'angle', 'mission',)

class ModalTileAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'picture', 'parent',)
    list_filter  = ('name', 'season', 'parent',)

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'top', 'left', 'angle', 'dropped',)
    list_filter  = ('name', 'color', 'top', 'left', 'angle',)

class ModalObjectiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'color',)
    list_filter  = ('name', 'season', 'color',)

class SpawnAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'top', 'left', 'angle', 'dropped',)
    list_filter  = ('name', 'color', 'top', 'left', 'angle',)  

class ModalSpawnAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'color',)
    list_filter  = ('name', 'season', 'color',)    

class DoorAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'state', 'top', 'left', 'angle', 'dropped',)
    list_filter  = ('name', 'color', 'state', 'top', 'left', 'angle',)

class ModalDoorAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'color', 'state',)
    list_filter  = ('name', 'season', 'color', 'state',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'top', 'left', 'angle', 'dropped',)
    list_filter  = ('name', 'color', 'top', 'left', 'angle',)

class ModalCarAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'type',)
    list_filter  = ('name', 'season', 'type',)

class NoiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'top', 'left', 'angle', 'dropped',)
    list_filter  = ('name', 'color', 'top', 'left', 'angle',)

class ModalNoiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'type',)
    list_filter  = ('name', 'season', 'type',)

class ExitAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'top', 'left', 'angle', 'dropped',)
    list_filter  = ('name', 'color', 'top', 'left', 'angle',)

class ModalExitAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'type',)
    list_filter  = ('name', 'season', 'type',)

# class GeneralTokenAdmin(admin.ModelAdmin):
#     list_display = ('name', 'color', 'type', 'top', 'left', 'angle', 'dropped',)
#     list_filter  = ('name', 'color', 'type', 'top', 'left', 'angle',)

# class ModalGeneralTokenAdmin(admin.ModelAdmin):
#     list_display = ('name', 'season', 'type',)
#     list_filter  = ('name', 'season', 'type',)

admin.site.register(Mission, MissionAdmin)
admin.site.register(Tile, TileAdmin)
admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Spawn, SpawnAdmin)
admin.site.register(Door, DoorAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Exit, ExitAdmin)
admin.site.register(Noise, NoiseAdmin)
# admin.site.register(GeneralToken, GeneralTokenAdmin)

admin.site.register(ModalTile, ModalTileAdmin)
admin.site.register(ModalDoor, ModalDoorAdmin)
admin.site.register(ModalObjective, ModalObjectiveAdmin)
admin.site.register(ModalSpawn, ModalSpawnAdmin)
admin.site.register(ModalCar, ModalCarAdmin)
admin.site.register(ModalNoise, ModalNoiseAdmin)
admin.site.register(ModalExit, ModalExitAdmin)
