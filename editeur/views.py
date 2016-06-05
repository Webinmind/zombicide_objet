 # -*- coding: utf-8 -*-
from zombicide_objet import settings
import os
from django.core import serializers
from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import UpdateView, FormView
from django.db.models import Count
from models import *
from forms import *
from django.core.files import File
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response,redirect
from django.http import HttpResponseRedirect,HttpResponse
# from reportlab.pdfgen import canvas
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont,TTFontFile,TTFError
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Frame
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.enums import TA_CENTER
# from reportlab.lib.units import inch, cm
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.colors import Color

def folder_menu(context):
    # Tiles
    modalTiles = ModalTile.objects.all().order_by('parent')
    returnTiles = []
    i=0
    for tile in modalTiles:
        tileTab = []
        tileTab.append(modalTiles[i])
        tileTab.append(modalTiles[i+1])
        returnTiles.append(tileTab)
        if (i+3)<=len(modalTiles):
            i+=2
        else:
            break

    context['season_one_tiles'] = returnTiles
    context['season_one_tiles_json'] = serializers.serialize('json', modalTiles)

    # Doors
    modalDoors = ModalDoor.objects.all().order_by('name')
    returnDoors = []
    i=0
    for door in modalDoors:
        doorTab = []
        doorTab.append(modalDoors[i])
        doorTab.append(modalDoors[i+1])
        returnDoors.append(doorTab)
        if (i+3)<=len(modalDoors):
            i+=2
        else:
            break

    context['season_one_doors'] = returnDoors
    # context['season_one_doors_json'] = serializers.serialize('json', modalDoors)

    # Objectives
    modalObjectives = ModalObjective.objects.all().order_by('name')
    context['season_one_objectives'] = modalObjectives
    # context['season_one_objectives_json'] = serializers.serialize('json', modalObjectives)

    # Spawns
    modalSpawns = ModalSpawn.objects.all().order_by('name')
    context['season_one_spawns'] = modalSpawns
    # context['season_one_spawns_json'] = serializers.serialize('json', modalSpawns)

    # Cars
    modalCars = ModalCar.objects.all().order_by('name')
    context['season_one_cars'] = modalCars
    # context['season_one_cars_json'] = serializers.serialize('json', modalCars)

    # Noise token
    modalNoise = ModalNoise.objects.all()
    context['season_one_noise'] = modalNoise
    # context['season_one_noise_json'] = serializers.serialize('json', modalNoise)
    
    # Exit tokens
    modalExit = ModalExit.objects.all()
    context['season_one_exit'] = modalExit
    # context['season_one_exit_json'] = serializers.serialize('json', modalExit)

    return context

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context = folder_menu(context)
        context['missions'] = Mission.objects.filter(active=True)
        return context

class NewmissionView(TemplateView):
    template_name = "newmission.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context = folder_menu(context)
        context['missions'] = Mission.objects.filter(active=True)
        return context

    def get(self, request):
        newmission = Mission.objects.create(name="Mission Tmp")
        newmission.save()
        return redirect(newmission)

class MissionView(TemplateView):
    template_name="mission.html"

    def get_context_data(self, **kwargs):
        context = super(MissionView, self).get_context_data(**kwargs)

        context = folder_menu(context)

        context['missions'] = Mission.objects.filter(active=True)
        context['form'] = MissionForm

        # Current mission
        mission = Mission.objects.filter(pk=kwargs['pk']).first()
        context['mission'] = mission
        context['missionjson'] = serializers.serialize('json', Mission.objects.filter(pk=kwargs['pk']))
        
        # Tiles already dropped
        dropped_tiles = Tile.objects.filter(mission=mission, dropped=True)
        context['dropped_tiles'] = dropped_tiles        
        context['dropped_tiles_json'] = serializers.serialize('json', dropped_tiles)
        
        # Tokens already dropped
        dropped_doors = Door.objects.filter(mission=mission, dropped=True)
        context['dropped_doors'] = dropped_doors
        context['dropped_doors_json'] = serializers.serialize('json',Door.objects.filter(mission=mission, dropped=True))

        # Objectives already dropped
        dropped_objectives = Objective.objects.filter(mission=mission, dropped=True)
        context['dropped_objectives'] = dropped_objectives
        context['dropped_objectives_json'] = serializers.serialize('json',Objective.objects.filter(mission=mission, dropped=True))
        
        # Spawns already dropped
        dropped_spawns = Spawn.objects.filter(mission=mission, dropped=True)
        context['dropped_spawns'] = dropped_spawns
        context['dropped_spawns_json'] = serializers.serialize('json',Spawn.objects.filter(mission=mission, dropped=True))
        
        # Cars already dropped
        dropped_cars = Car.objects.filter(mission=mission, dropped=True)
        context['dropped_cars'] = dropped_cars
        context['dropped_cars_json'] = serializers.serialize('json',Car.objects.filter(mission=mission, dropped=True))
        
        # Noises already dropped
        dropped_noises = Noise.objects.filter(mission=mission, dropped=True)
        context['dropped_noises'] = dropped_noises
        context['dropped_noises_json'] = serializers.serialize('json',Noise.objects.filter(mission=mission, dropped=True))
        
        # Exits already dropped
        dropped_exits = Exit.objects.filter(mission=mission, dropped=True)
        context['dropped_exits'] = dropped_exits
        context['dropped_exits_json'] = serializers.serialize('json',Exit.objects.filter(mission=mission, dropped=True))

        # Number of tokens placed, grouped by type
        # Objectives
        objectives_in_use = Objective.objects.filter(dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['objectives_in_use'] = objectives_in_use
        
        objs_in_use=[]
        for objective in objectives_in_use:
            objs_in_use.append({objective['ref'].encode('utf-8'):objective['total']})
        context['number_objectives']=objs_in_use
        
        # Doors
        doors_in_use = Door.objects.filter(dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['doors_in_use'] = doors_in_use

        nb_doors=[]
        for door in doors_in_use:
            nb_doors.append({door['ref'].encode('utf-8'):door['total']})
        context['number_doors']=nb_doors
        
        # Spawns
        spawns_in_use = Spawn.objects.filter(dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['spawns_in_use'] = spawns_in_use

        nb_spawns=[]
        for spawn in spawns_in_use:
            nb_spawns.append({spawn['ref'].encode('utf-8'):spawn['total']})
        context['number_spawns']=nb_spawns
        
        # Cars
        cars_in_use = Car.objects.filter(dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['cars_in_use'] = cars_in_use

        nb_cars=[]
        for car in cars_in_use:
            nb_cars.append({car['ref'].encode('utf-8'):car['total']})
        context['number_cars']=nb_cars
        
        # Noises
        noises_in_use = Noise.objects.filter(dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['noises_in_use'] = noises_in_use

        nb_noises=[]
        for noise in noises_in_use:
            nb_noises.append({noise['ref'].encode('utf-8'):noise['total']})
        context['number_noises']=nb_noises

        # Exits
        exits_in_use = Exit.objects.filter(dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['exits_in_use'] = exits_in_use

        nb_exits=[]
        for exit in exits_in_use:
            nb_exits.append({exit['ref'].encode('utf-8'):exit['total']})
        context['number_exits']=nb_exits

        return context

class SavemissionView(UpdateView):
    
    def post(self,request):
        if self.request.is_ajax():
            mission_id   = request.POST.get('mission_id',65536)
            mission_name = request.POST.get('mission_name','Mission Tmp')
            mission_difficulty = request.POST.get('mission_difficulty','easy')
            mission_players = request.POST.get('nb_of_player','6')
            mission_time = request.POST.get('mission_time','60mn')
            mission_resume = request.POST.get('mission_resume','Racontez ce qui les attend !!')
            mission_objectives = request.POST.get('mission_objectives','Racontez ce qu\'ils doivent faire pour gagner !!')

            mission, created = Mission.objects.get_or_create(pk=mission_id)
            mission.name = mission_name
            mission.difficulty = mission_difficulty
            mission.resume = mission_resume
            mission.objectives = mission_objectives
            mission.nb_of_player = mission_players
            mission.mission_time = mission_time

            mission.save()
            return redirect(mission)

class PdfView(TemplateView):
    template_name="pdf.html"

    def get_context_data(self, **kwargs):
        context                    = super(TemplateView, self).get_context_data(**kwargs)
        context                    = folder_menu(context)
        context['current_mission'] = Mission.objects.get(pk=kwargs['mission_id'])
        context['missionjson']     = serializers.serialize('json', Mission.objects.filter(pk=kwargs['mission_id']))
        context['used_tiles']      = Tile.objects.filter(mission=kwargs['mission_id'], dropped=True).order_by('top','left')
        context['used_doors']      = Door.objects.filter(mission=kwargs['mission_id'], dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['used_objectives'] = Objective.objects.filter(mission=kwargs['mission_id'], dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['used_spawns']     = Spawn.objects.filter(mission=kwargs['mission_id'], dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['used_cars']       = Car.objects.filter(mission=kwargs['mission_id'], dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['used_noises']     = Noise.objects.filter(mission=kwargs['mission_id'], dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['used_exits']      = Exit.objects.filter(mission=kwargs['mission_id'], dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        context['missions']        = Mission.objects.filter(active=True)
        return context

class ExportToPdfView(View):

    def drawGrid(self,p):
        p.setFont('RobotoRegular', 10)
        for i in range(30):
            p.drawString(i*cm,0,str(i))
            p.drawString(i*cm,29.4*cm,str(i))
            p.drawString(0,i*cm,str(i))
            p.drawString(20.5*cm,i*cm,str(i))
            path = p.beginPath()
            p.setLineWidth(0.5)
            blackAlpha = Color( 0, 0, 0, alpha=0.1)
            p.setStrokeColor(blackAlpha)
            
            path.moveTo(i*cm,0*cm)
            path.lineTo(i*cm,29.7*cm)

            path.moveTo(0*cm,i*cm)
            path.lineTo(21*cm,i*cm)

            path.close()
            p.drawPath(path)

    def prepareTilesDatas(self,p,tilesArray):
        # Rescale :
        # (max'-min')/(max-min)*(v-max)+max'
        # (max'-min')/(max-min)*(v-min)+min'
        
        tileWidth = tileHeight = 4
        for tile in tilesArray:
            tile_left = tile.left-15
            tile_top = tile.top
            tile_angle = str(tile.angle % 360)
            newLeft = tile_left*16/1000
            newTop = tile_top*16/1000

            filename = '/var/www/zombicide/editeur/static/imgs/tiles/season_one/tiles/tiles_rotate/'+tile.name+'_'+tile_angle+'.png'
            p.saveState()
            p.translate(newLeft*cm,newTop*cm)
            p.scale(1,-1)
            p.drawImage(filename, 0,0, tileWidth*cm, -tileHeight*cm)
            p.restoreState()
            
    def prepareObjectivesDatas(self,p,objectivesArray):
        for objective in objectivesArray:
            objective_left = objective.left-15
            objective_top = objective.top
            objective_angle = str(objective.angle % 360)
            newLeft = objective_left*16/1000
            newTop = objective_top*16/1000

            objectiveSize = 0.448
            filename = '/var/www/zombicide/editeur/static/imgs/tiles/season_one/objectives/'+objective.ref.replace('objective_','')+'.png'
            p.saveState()
            p.translate(newLeft*cm,newTop*cm)
            p.scale(1,-1)
            p.drawImage(filename, 0,0, objectiveSize*cm, -objectiveSize*cm)
            p.restoreState()
            
    def prepareDoorsDatas(self,p,doorsArray):
        for door in doorsArray:
            door_angle = str(door.angle % 360)
            doorWidth  = 0.48 if door_angle=='90' or door_angle=='270' else 0.544
            doorHeight = 0.544 if door_angle=='90' or door_angle=='270' else 0.48
            door_left = (door.left+doorWidth)-15
            topOffset = (doorHeight-doorWidth)/2 if door_angle=='90' or door_angle=='270' else 0
            leftOffset = (doorHeight-doorWidth)/2 if door_angle=='90' or door_angle=='270' else 0
            door_top = door.top+doorHeight
            newLeft = (door_left*16/1000)+leftOffset
            newTop = (door_top*16/1000)-topOffset
            
            filename = '/var/www/zombicide/editeur/static/imgs/tiles/season_one/doors/doors_rotate/'+door.ref.replace('door_','')+'_'+door_angle+'.png'
            p.saveState()
            p.translate(newLeft*cm,newTop*cm)
            p.scale(1,-1)
            p.drawImage(filename, 0,0, doorWidth*cm, -doorHeight*cm)
            p.restoreState()

    def prepareCarsDatas(self,p,carsArray):
        for car in carsArray:
            car_angle = str(car.angle % 360)
            carWidth  = 1.632 if car_angle=='90' or car_angle=='270' else 0.832
            carHeight = 0.832 if car_angle=='90' or car_angle=='270' else 1.632
            topOffset = (carHeight-carWidth)/2 if car_angle=='90' or car_angle=='270' else 0
            leftOffset = (carHeight-carWidth)/2 if car_angle=='90' or car_angle=='270' else 0
            car_left = (car.left+carWidth)-15
            car_top = car.top+carHeight
            newLeft = (car_left*16/1000)+leftOffset
            newTop = (car_top*16/1000)-topOffset
            
            filename = '/var/www/zombicide/editeur/static/imgs/tiles/season_one/cars/cars_rotate/'+car.ref.replace('car_','')+'_'+car_angle+'.png'
            p.saveState()
            p.translate(newLeft*cm,newTop*cm)
            p.scale(1,-1)
            p.drawImage(filename, 0,0, carWidth*cm, -carHeight*cm)
            p.restoreState()

    def prepareSpawnsDatas(self,p,spawnsArray):
        for spawn in spawnsArray:
            spawn_angle = str(spawn.angle % 360)
            leftOffset=0
            topOffset=0
            if(spawn.ref.replace('spawn_','')=='start'):
                spawnWidth  = 0.64
                spawnHeight = 0.624
            else:
                spawnWidth  = 0.416 if spawn_angle=='90' or spawn_angle=='270' else 0.816
                spawnHeight = 0.816 if spawn_angle=='90' or spawn_angle=='270' else 0.416
                topOffset = (spawnHeight-spawnWidth)/2 if spawn_angle=='90' or spawn_angle=='270' else 0
                leftOffset = (spawnHeight-spawnWidth)/2 if spawn_angle=='90' or spawn_angle=='270' else 0
            
            spawn_left = (spawn.left+spawnWidth)-15
            spawn_top = spawn.top+spawnHeight
            newLeft = (spawn_left*16/1000)+leftOffset
            newTop = (spawn_top*16/1000)-topOffset
            
            filename = '/var/www/zombicide/editeur/static/imgs/tiles/season_one/spawn/spawn_rotate/'+spawn.ref+'_'+spawn_angle+'.png'
            p.saveState()
            p.translate(newLeft*cm,newTop*cm)
            p.scale(1,-1)
            p.drawImage(filename, 0,0, spawnWidth*cm, -spawnHeight*cm)
            p.restoreState()

    def prepareExitDatas(self,p,exitsArray):
        for exit in exitsArray:
            name = exit.ref.replace('exit_','')
            exit_angle = str(exit.angle % 360)
            exitWidth  = 0.416 if exit_angle=='90' or exit_angle=='270' else 0.816
            exitHeight = 0.816 if exit_angle=='90' or exit_angle=='270' else 0.416
            topOffset = (exitHeight-exitWidth)/2 if exit_angle=='90' or exit_angle=='270' else 0
            leftOffset = (exitHeight-exitWidth)/2 if exit_angle=='90' or exit_angle=='270' else 0
            exit_left = (exit.left+exitWidth)-15
            exit_top = exit.top+exitHeight
            newLeft = (exit_left*16/1000)+leftOffset
            newTop = (exit_top*16/1000)-topOffset
            
            filename = '/var/www/zombicide/editeur/static/imgs/tiles/season_one/'+name+'/rotate/'+name+'_'+exit_angle+'.png'
            p.saveState()
            p.translate(newLeft*cm,newTop*cm)
            p.scale(1,-1)
            p.drawImage(filename, 0,0, exitWidth*cm, -exitHeight*cm)
            p.restoreState()

    def prepareNoiseDatas(self,p,noisesArray):
        for noise in noisesArray:
            name = noise.ref.replace('noise_','')
            noise_angle = str(noise.angle % 360)
            noiseWidth  = 0.336 if noise_angle=='90' or noise_angle=='270' else 0.368
            noiseHeight = 0.368 if noise_angle=='90' or noise_angle=='270' else 0.336
            
            noise_left = (noise.left+noiseWidth)-15
            noise_top = noise.top+noiseHeight
            newLeft = noise_left*16/1000
            newTop = noise_top*16/1000
            
            filename = '/var/www/zombicide/editeur/static/imgs/tiles/season_one/'+name+'/rotate/'+name+'_'+noise_angle+'.png'
            p.saveState()
            p.translate(newLeft*cm,newTop*cm)
            p.scale(1,-1)
            p.drawImage(filename, 0,0, noiseWidth*cm, -noiseHeight*cm, mask='auto')
            p.restoreState()

    def prepareTokensInUseDatas(self,p, lastY, mission_id):
        # Tokens background
        p.setFillColor('#d3d3d3')
        p.setStrokeColor('White')
        p.rect(0,lastY*cm,9*cm,4.5*cm, fill=1)
        cursor = lastY

        # Doors in use
        cursor+=0.2
        doors = Door.objects.filter(mission=mission_id, dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        i=0
        for door in doors:
            name = door['ref'].replace('door_','')
            p.saveState()
            p.translate((i+0.2)*cm, (cursor+0.55)*cm)
            p.scale(1,-1)
            (width, height) = p.drawImage('/var/www/zombicide/editeur/static/imgs/tiles/season_one/doors/'+name+'.png', 0, 0, 0.55*cm, 0.48*cm) 
            p.translate((-i-0.2)*cm, (-cursor-0.55)*cm)
            p.restoreState()
            i+=1
        
        # Objectives in use
        cursor+=0.8
        objectives = Objective.objects.filter(mission=mission_id, dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        i=0
        width=0
        height=0
        for objective in objectives:
            name = objective['ref'].replace('objective_','')
            (width, height) = p.drawImage('/var/www/zombicide/editeur/static/imgs/tiles/season_one/objectives/'+name+'.png', (i+0.2)*cm, cursor*cm, 0.55*cm, 0.55*cm) 
            i+=1
        
        # Spawns in use
        cursor+=0.7
        spawns = Spawn.objects.filter(mission=mission_id, dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        i=0
        for spawn in spawns:
            name = spawn['ref'].replace('spawn_','')
            if name=='start':
                sWidth  = 0.8 
                sHeight = 0.8
                sTop = cursor
            else:
                sWidth  = 0.82 
                sHeight = 0.42
                sTop = cursor+0.2
            p.saveState()
            p.translate((i+0.2)*cm, (sTop+sHeight)*cm)
            p.scale(1,-1)
            (width, height) = p.drawImage('/var/www/zombicide/editeur/static/imgs/tiles/season_one/spawn/spawn_'+name+'.png', 0, 0, sWidth*cm, sHeight*cm) 
            p.translate((-i-0.2)*cm, (-sTop-sHeight)*cm)
            p.restoreState()
            i+=1

        # Cars in use
        cursor+=0.9
        cars = Car.objects.filter(mission=mission_id, dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        i=0
        for car in cars:
            name = car['ref'].replace('car_','')
            sWidth  = 0.42 
            sHeight = 0.82
            sTop = cursor
            p.saveState()
            p.translate(((i*0.8)+0.2)*cm, (sTop+sHeight)*cm)
            p.scale(1,-1)
            (width, height) = p.drawImage('/var/www/zombicide/editeur/static/imgs/tiles/season_one/cars/'+name+'.png', 0, 0, sWidth*cm, sHeight*cm) 
            p.translate((-i-0.2)*cm, (-sTop-sHeight)*cm)
            p.restoreState()
            i+=1
        
        # Noises in use
        cursor+=1.2
        noises = Noise.objects.filter(mission=mission_id, dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        i=0
        for noise in noises:
            name = noise['ref'].replace('noise_','')
            sWidth  = 0.368
            sHeight = 0.336
            sTop = cursor
            p.saveState()
            p.translate((i+0.2)*cm, (sTop+sHeight)*cm)
            p.scale(1,-1)
            (width, height) = p.drawImage('/var/www/zombicide/editeur/static/imgs/tiles/season_one/'+name+'/'+name+'.png', 0, 0, sWidth*cm, sHeight*cm, mask='auto') 
            p.translate((-i-0.2)*cm, (-sTop-sHeight)*cm)
            p.restoreState()
            i+=1

        # Exits in use
        exits = Exit.objects.filter(mission=mission_id, dropped=True).values('ref').annotate(total=Count('ref')).order_by('ref')
        i=0
        for exit in exits:
            name = exit['ref'].replace('exit_','')
            sWidth  = 0.82
            sHeight = 0.42
            sTop = cursor
            p.saveState()
            p.translate((i+0.8)*cm, (sTop+sHeight)*cm)
            p.scale(1,-1)
            (width, height) = p.drawImage('/var/www/zombicide/editeur/static/imgs/tiles/season_one/'+name+'/'+name+'.png', 0, 0, sWidth*cm, sHeight*cm, mask='auto') 
            p.translate((-i-0.8)*cm, (-sTop-sHeight)*cm)
            p.restoreState()
            i+=1
        return cursor

    def post(self, request):
        mission_id                 = request.POST.get('current_mission_id')
        current_mission            = Mission.objects.get(pk=mission_id)
        current_mission_name       = request.POST.get('mission_name')
        current_mission_number     = request.POST.get('mission_numero', mission_id)
        current_mission_resume     = request.POST.get('mission_resume')
        current_mission_special    = request.POST.get('mission_special')
        current_mission_difficulty = request.POST.get('mission_difficulty')
        current_mission_players    = request.POST.get('nb_of_player')
        current_mission_duration   = request.POST.get('mission_time')

        current_mission.name          = current_mission_name
        current_mission.number        = current_mission_number
        current_mission.resume        = current_mission_resume
        current_mission.special_rules = current_mission_special
        current_mission.difficulty    = current_mission_difficulty
        current_mission.nb_of_player  = current_mission_players
        current_mission.mission_time  = current_mission_duration
        current_mission.save()

        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="'+current_mission.name+'.pdf"'

        # Create the PDF object, using the response object as its "file."
        p = canvas.Canvas(response, pagesize=A4, bottomup=0)
        p.translate(cm,cm)
        styles = getSampleStyleSheet()
        styleN = styles['Normal']
        styleH = styles['Heading1']

        pdfmetrics.registerFont(TTFont("Roboto", 'Roboto-Black.ttf'))
        pdfmetrics.registerFont(TTFont("RobotoRegular", 'Roboto-Regular.ttf'))
        pdfmetrics.registerFont(TTFont("RobotoBold", 'Roboto-Bold.ttf'))
        pdfmetrics.registerFont(TTFont("Hand", 'JustAnotherHand.ttf'))
        pdfmetrics.registerFont(TTFont("Chaos", 'Chaos.ttf'))
        
        # GRILLE
        # self.drawGrid(p)

        p.setFont('Roboto', 51)
        p.setFillColor('Gray')

        # Mission number
        p.drawString(0,1.5*cm,'M'+str(current_mission.number))

        # Mission name
        p.setFillColor('Gold')
        id_length = p.stringWidth('M'+str(current_mission.number), fontName='Roboto', fontSize=48)
        nameArray = current_mission.name.split(' ')

        wordTop = []
        wordBottom = []

        i=0
        for word in nameArray:
            if i<=(len(nameArray)/2):
                wordTop.append(word)
            else:
                wordBottom.append(word)
            i+=1
        
        p.setFontSize(24)
        wordLength = 0
        top = 0.8
        for word in wordTop:
            p.drawString((id_length+20)+wordLength,top*cm,word+' ')
            wordLength += p.stringWidth(word+' ', fontName='Roboto', fontSize=24)

        wordLength = 0
        top = 1.5
        for word in wordBottom:
            p.drawString(id_length+20+wordLength,top*cm,word+' ')
            wordLength += p.stringWidth(word+' ', fontName='Roboto', fontSize=24)

        # Informations
        p.setFillColor('Gray')
        p.setFontSize(10)
        p.drawString(0,2.2*cm,current_mission.difficulty.upper()+' / '+current_mission.nb_of_player.upper()+' SURVIVORS / '+current_mission.mission_time.upper())

        # Summary
        p.setFont('Hand', 16)
        p.setFillColor('Black')
        resumeArray = current_mission.resume.split('\n')
        
        i=0
        lastY=3
        for r in resumeArray:
            lastY+=0.5*i
            p.drawString(0,lastY*cm,r)
            i+=1

        lastY+=1

        # Tiles in use
        p.setFont('RobotoRegular', 10)
        p.setFillColor('Black')
        p.drawString(0,lastY*cm,"Tiles needed : ")
        tiles_length = p.stringWidth('Tiles needed : ', fontName='RobotoRegular', fontSize=10)
        tiles = Tile.objects.filter(mission=mission_id, dropped=True).order_by('top','left')
        p.setFont('Roboto', 10)
        i = 0
        for tile in tiles:
            if(i==len(tiles)-1):
                p.drawString((tiles_length+5)+0.7*i*cm,lastY*cm,tile.name.upper())
            else:
                p.drawString((tiles_length+5)+0.7*i*cm,lastY*cm,tile.name.upper()+',')
                i+=1

        lastY+=0.5
        lastY = self.prepareTokensInUseDatas(p,lastY,mission_id)

        # Mission main objective
        lastY+=1.9
        p.setFont('Chaos', 18)
        p.setFillColor('Gray')
        p.drawString(0,lastY*cm,'OBJECTIVES')
        
        i=0
        lastY+=0.5
        objectiveArray = current_mission.objectives.split('\n')
        for objective in objectiveArray:
            objArray = objective.split(':')
            p.setFont('RobotoRegular', 10)
            p.setFillColor('Black')
            
            if len(objArray)==2:
                p.setFont('RobotoBold', 10)
                p.drawString(0*cm,(lastY+0.5*i)*cm,objArray[0]+' : ')
                textLength = p.stringWidth(objArray[0]+' : ', fontName='RobotoBold', fontSize=10)
                p.setFont('RobotoRegular', 10)
                p.drawString(textLength+(0.1*cm),(lastY+0.5*i)*cm,objArray[1]+'.')
            else:
                p.drawString(0*cm,(lastY+0.5*i)*cm,objArray[0]+'.')
            i+=1

        # Special Rules
        lastY+=2
        p.setFont('Chaos', 18)
        p.setFillColor('Gray')
        p.drawString(0,lastY*cm,'SPECIAL RULES')
        p.setFont('RobotoRegular', 10)
        specialArray = current_mission.special_rules.split('\n')
        
        i=0
        lastY+=0.5
        for specialrule in specialArray:
            ruleArray = specialrule.split(':')
            p.setFont('RobotoBold', 10)
            p.setFillColor('Black')
            if (len(ruleArray)>1):
                p.drawString(0,(lastY+0.5*i)*cm,'.  '+ruleArray[0]+'.')
            else:
                p.setFont('RobotoRegular', 10)
                p.drawString(0,(lastY+0.5*i)*cm,ruleArray[0]+'.')
            if (len(ruleArray)>1):
                rLength = p.stringWidth(ruleArray[0], fontName='RobotoRegular', fontSize=10)
                p.setFont('RobotoRegular', 10)
                p.drawString(rLength+0.5*cm,(lastY+0.5*i)*cm,ruleArray[-1])
            i+=1

        p.showPage()
        
        # NEW PAGE
        p.translate(cm,cm)
        # GRILLE 
        # self.drawGrid(p)
        
        self.prepareTilesDatas(p,tiles)
            
        # Dessin des Tokens
        # Doors
        doors = Door.objects.filter(mission=mission_id, dropped=True)
        self.prepareDoorsDatas(p,doors)
        
        # Objectives
        objectives = Objective.objects.filter(mission=mission_id, dropped=True)
        self.prepareObjectivesDatas(p,objectives)
        
        # Cars
        cars = Car.objects.filter(mission=mission_id, dropped=True)
        self.prepareCarsDatas(p,cars)
        
        # Spawns
        spawns = Spawn.objects.filter(mission=mission_id, dropped=True)
        self.prepareSpawnsDatas(p,spawns)
        
        # Noises
        noises = Noise.objects.filter(mission=mission_id, dropped=True)
        self.prepareNoiseDatas(p,noises)
        
         # Exits
        exits = Exit.objects.filter(mission=mission_id, dropped=True)
        self.prepareExitDatas(p,exits)
        
        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()

        return response
    
class AddTilesDatasView(UpdateView):
    
    def post(self,request):
        if self.request.is_ajax():
            name  = request.POST.get('id')
            mission_id  = request.POST.get('mission',0)
            
            mission, created = Mission.objects.get_or_create(pk=mission_id)
            
            tileToChange, created = Tile.objects.get_or_create(name=name, 
                                                               mission=mission)
            tileToChange.dropped = True
            tileToChange.save()

            return HttpResponseRedirect('/')

class UpdateTilesDatasView(UpdateView):

    def post(self,request):
        if self.request.is_ajax():
            name  = request.POST.get('id')
            mission_id = request.POST.get('mission',0)
            top        = request.POST.get('top',0)
            parent     = request.POST.get('parent','A')
            left       = request.POST.get('left',0)
            angle      = request.POST.get('angle',0)

            mission, created = Mission.objects.get_or_create(pk=mission_id) 
            tileToChange, created = Tile.objects.get_or_create(name=name, 
                                                               mission=mission,
                                                               defaults={'top':top,
                                                                         'left':left,
                                                                         'angle':angle,
                                                                         'parent':parent}) 

            tileToChange.top     = top
            tileToChange.left    = left
            tileToChange.angle   = angle
            tileToChange.parent  = parent
            tileToChange.dropped = True
            tileToChange.mission = mission
            tileToChange.save()

            # Get dropped tile with same parent
            droppedTile = Tile.objects.filter(parent=parent, dropped=True).exclude(name=name).first()
            if droppedTile:
                droppedTile.dropped = False
                droppedTile.save()

        return HttpResponseRedirect('/')

class RemoveTilesDatasView(UpdateView):
    def post(self,request):
        if self.request.is_ajax():
            name  = request.POST.get('id')
            mission_id  = request.POST.get('mission',0)
            unactivetilesArray = request.POST.get('unactivetiles')
            
            mission = Mission.objects.get(pk=mission_id)
            try:
                tileToChange = Tile.objects.get(name=name, 
                                                mission=mission)
                tileToChange.dropped = False
                tileToChange.save()
            except:
                pass

            return HttpResponseRedirect('/')
            
class UpdateTokensDatasView(UpdateView):

    def post(self,request):
        if self.request.is_ajax():
            name  = request.POST.get('id')
            ref    = request.POST.get('modeleid')
            type  = request.POST.get('type')
            color = request.POST.get('color','red')
            state       = request.POST.get('state','closed')
            mission_id  = request.POST.get('mission',0)
            top         = request.POST.get('top',0)
            left        = request.POST.get('left',0)
            angle       = request.POST.get('angle',0)

            mission, created = Mission.objects.get_or_create(pk=mission_id) 

            if(type=='door'):
               tokenToChange, created = Door.objects.get_or_create(ref=ref,
                                                                    name=name, 
                                                                    mission=mission,
                                                                    dropped=True,
                                                                    color=color,
                                                                    defaults={'top':top,
                                                                              'left':left,
                                                                              'angle':angle,
                                                                              'dropped':True})

            if(type=='objective'):
                tokenToChange, created = Objective.objects.get_or_create(ref=ref,
                                                                         name=name,
                                                                         mission=mission,
                                                                         dropped=True,
                                                                         color=color,
                                                                         defaults={'top':top,
                                                                                   'left':left,
                                                                                   'angle':angle,
                                                                                   'dropped':True})

            if(type=='spawn'):
                tokenToChange, created = Spawn.objects.get_or_create(ref=ref,
                                                                     name=name,
                                                                     mission=mission,
                                                                     dropped=True,
                                                                     color=color,
                                                                     defaults={'top':top,
                                                                               'left':left,
                                                                               'angle':angle,
                                                                               'dropped':True})

            if(type=='car'):
                tokenToChange, created = Car.objects.get_or_create(ref=ref,
                                                                   name=name,
                                                                   mission=mission,
                                                                   dropped=True,
                                                                   color=color,
                                                                   defaults={'top':top,
                                                                             'left':left,
                                                                             'angle':angle,
                                                                             'dropped':True})

            if(type=='noise'):
                tokenToChange, created = Noise.objects.get_or_create(name=name, 
                                                                     ref=ref,
                                                                     mission=mission,
                                                                     dropped=True,
                                                                     type=type,
                                                                     defaults={'top':top,
                                                                               'left':left,
                                                                               'angle':angle,
                                                                               'dropped':True})

            if(type=='exit'):
                tokenToChange, created = Exit.objects.get_or_create(name=name, 
                                                                    ref=ref,
                                                                    mission=mission,
                                                                    dropped=True,
                                                                    type=type,
                                                                    defaults={'top':top,
                                                                              'left':left,
                                                                              'angle':angle,
                                                                              'dropped':True})
            
            tokenToChange.dropped       = True
            tokenToChange.name    = name
            tokenToChange.ref      = ref
            tokenToChange.top           = top
            tokenToChange.left          = left
            tokenToChange.angle         = angle
            tokenToChange.color   = color
            tokenToChange.mission       = mission
            tokenToChange.save()

        return HttpResponseRedirect('/')

class RemoveTokensDatasView(UpdateView):
    
    def post(self,request):
        if self.request.is_ajax():
            id  = request.POST.get('id')
            token_modeleid    = request.POST.get('modeleid')
            type  = request.POST.get('tokenType')
            mission_id  = request.POST.get('mission',0)
            type  = request.POST.get('type')
            color = request.POST.get('color')
            state       = request.POST.get('state')

            mission = Mission.objects.get(pk=mission_id)
            try:
                if(type=='door'):
                    tokensToChange = Door.objects.filter(id=id, mission=mission)

                if(type=='objective'):
                    tokensToChange = Objective.objects.filter(id=id, mission=mission)
                    
                if(type=='spawn'):
                    tokensToChange = Spawn.objects.filter(id=id, mission=mission)

                if(type=='car'):
                    tokensToChange = Car.objects.filter(id=id, mission=mission)

                if(type=='noise'):
                    tokensToChange = Noise.objects.filter(id=id, 
                                                          type=type,
                                                          mission=mission)

                if(type=='exit'):
                    tokensToChange = Exit.objects.filter(id=id, 
                                                         type=type,
                                                         mission=mission)
                
                for tokenToChange in tokensToChange:
                    tokenToChange.dropped = False
                    tokenToChange.save()
            except:
                print '*** Exception : No Token found ***', mission_id, type, id
                
            return HttpResponseRedirect('/')

class RemoveTokensUIView(UpdateView):

    def post(self,request):
        if self.request.is_ajax():
            name  = request.POST.get('name')
            type  = request.POST.get('tokenType')
            mission_id  = request.POST.get('mission',0)
            mission = Mission.objects.get(pk=mission_id)
            try:
                if(type=='door'):
                    tokenToChange = Door.objects.get(name=name, mission=mission)

                if(type=='objective'):
                    tokenToChange = Objective.objects.get(name=name, mission=mission)
                    
                if(type=='spawn'):
                    tokenToChange = Spawn.objects.get(name=name, mission=mission)

                if(type=='car'):
                    tokenToChange = Car.objects.get(name=name, mission=mission)

                if(type=='noise'):
                    tokenToChange = Noise.objects.get(name=name, 
                                                      type=type,
                                                      mission=mission)

                if(type=='exit'):
                    tokenToChange = Exit.objects.get(name=name, 
                                                     type=type,
                                                     mission=mission)
                
                tokenToChange.dropped = False
                tokenToChange.save()
            except:
                print '*** Exception : No Token found ***', mission_id, type, name
                
            return HttpResponseRedirect('/')

class AddTokensDatasView(UpdateView):

    def post(self,request):
        if self.request.is_ajax():
            name  = request.POST.get('id')
            ref  = request.POST.get('modeleid')
            type  = request.POST.get('type')
            color  = request.POST.get('color')
            token_state  = request.POST.get('state')
            mission_id  = request.POST.get('mission',0)

            # Faut essayer
            # types = {'door':Door, 'objective':Objective, 'spawn':Spawn, 'car':Car, 'noise':Noise, 'exit':Exit}
            # proto = types[type].__class__
            # print '*** proto ***', proto
            # *** proto *** <class 'django.db.models.base.ModelBase'>; moi je veux Door, Spawn,...
            # tokenToChange, created = proto.objects.get_or_create(name=name, 
            #                                                      id=id,
            #                                                      mission=mission,
            #                                                      defaults={'color':color})




            mission, created = Mission.objects.get_or_create(pk=mission_id)
            if(type=='door'):
                tokenToChange, created = Door.objects.get_or_create(name=name,
                                                                    ref=ref, 
                                                                    mission=mission,
                                                                    defaults={'color':color,
                                                                             'state':token_state})
            if(type=='objective'):
                tokenToChange, created = Objective.objects.get_or_create(name=name, 
                                                                         ref=ref,
                                                                         mission=mission,
                                                                         defaults={'color':color})
            if(type=='spawn'):
                tokenToChange, created = Spawn.objects.get_or_create(name=name, 
                                                                     ref=ref,
                                                                     mission=mission,
                                                                     defaults={'color':color})
            if(type=='car'):
                tokenToChange, created = Car.objects.get_or_create(name=name, 
                                                                   ref=ref,
                                                                   mission=mission,
                                                                   defaults={'color':color})

            if(type=='noise'):
                tokenToChange, created = Noise.objects.get_or_create(name=name, 
                                                                     ref=ref,
                                                                     mission=mission,
                                                                     type=ref,
                                                                     defaults={'color':color})

            if(type=='exit'):
                tokenToChange, created = Exit.objects.get_or_create(name=name, 
                                                                    ref=ref,
                                                                    mission=mission,
                                                                    type=type,
                                                                    defaults={'color':color})
            
            tokenToChange.dropped = True
            tokenToChange.save()

            return HttpResponseRedirect('/')

class HelpView(TemplateView):
    template_name='help.html'

    def get_context_data(self, **kwargs):
        context = super(HelpView, self).get_context_data(**kwargs)
        context['missions'] = Mission.objects.filter(active=True)
        return context
        
        
class FactoryView(TemplateView):
    template_name = "factory.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context = folder_menu(context)
        context['missions'] = Mission.objects.filter(active=True)
        return context