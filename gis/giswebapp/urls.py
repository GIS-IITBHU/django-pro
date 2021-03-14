from django.conf.urls import include,url

from .views import HomePageView, hostels_datasets,point_datasets

urlpatterns = [
	url(r'^$', HomePageView.as_view(), name = 'home'),
	url(r'^hostels_data/$', hostels_datasets , name = 'hostels'),
	url(r'^incidence_data/$', point_datasets, name = 'incidences'),


]