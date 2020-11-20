from django.shortcuts import render
from .models import playername,teamnames, match
from django.http import HttpResponse
import json
from django.views.generic import ListView, DetailView, View



class HomeView(ListView):
    model = match
    template_name = "dashboard.html"
    
    ordering = ['-match_number']


class Teams(ListView):
    model = teamnames
    template_name ="teamdetails.html"