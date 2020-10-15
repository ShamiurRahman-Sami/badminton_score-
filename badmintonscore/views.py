from django.shortcuts import render
from .models import playername,teamnames
from django.http import HttpResponse
import json


def get_playername(request):
    id = request.GET.get('id', '')
    result = list(playername.objects.filter(
    teamnames_id=int(id)).values('id', 'team_name'))
    return HttpResponse(json.dumps(result), content_type="application/json")