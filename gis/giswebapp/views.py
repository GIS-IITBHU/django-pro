from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Hostels,Incidences
# Create your views here.
class HomePageView(TemplateView):
	template_name = 'index.html'

def hostels_datasets(request):
	hostels = serialize('geojson', Hostels.objects.all())
	return HttpResponse(hostels,content_type='json')

def point_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points,content_type='json')