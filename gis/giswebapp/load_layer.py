import os
from django.contrib.gis.utils import LayerMapping
from .models import Hostels

hostels_mapping = {
    'name': 'Name',
    'country': 'Country',
    'hostelid': 'HostelID',
    'geom': 'MULTIPOLYGON',
}

hostels_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/Hostels.shp'))


def run(verbose=True):
    lm = LayerMapping(Hostels,hostels_shp,hostels_mapping, transform=False, encoding='utf-8')
    lm.save(strict =True,verbose=verbose)
