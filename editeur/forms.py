# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Mission

# Create the form class.
class MissionForm(ModelForm):
    class Meta:
        model = Mission
        fields = ['name', 'resume']