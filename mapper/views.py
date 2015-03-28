from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse

import overpass
import geojson
from geographiclib.geodesic import Geodesic
from requests import get
import xml.etree.ElementTree as ET




class MainPage(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request,'index.html')




class OverpassApiAjax(View):

    def get(self,request,*args,**kwargs):
        api = overpass.API()
        around = str(request.GET.get('around', '2500'))
        lat0 = str(request.GET.get('lat', 42))
        lon0 = str(request.GET.get('lon', -92))
        lat1 = str(request.GET.get('lat1', 0))  # means that 0 is the default if 'lat1' is not included
        lon1 = str(request.GET.get('lon1', 0))
        if lat1 == '0' or lon1 == '0':
            around = str(2000)
        else:
            l = Geodesic.WGS84.Inverse(float(lat0), float(lon0), float(lat1), float(lon1))
            around = str(l['s12']) if l['s12'] < 6000 else str(6000)
        LatLonString = lat0 + "," + lon0 + ")"
        r = api.Get('way(around:' + around + ',' + LatLonString + "[bicycle=yes]", asGeoJSON=True)
        return HttpResponse(geojson.dumps(r), content_type="application/json; charset='utf-8'")


class NiceRideAjax(View):
    def get(self, request, *args, **kwargs):
        r = get(url="https://secure.niceridemn.org/data2/bikeStations.xml")
        doc = ET.fromstring(r.text)
        stations = doc.findall('station')
        # this isn't really json it is a bunch of  python dicts inside a python list
        json = [{item.tag: item.text for item in station} for station in stations]  #look at that beauty there
        gj = []
        for d in json:
            if d['public']=='true':
                lat = d['lat']
                long = d['long']
                del d['lat']
                del d['long']
                gj.append({'type': 'Point', 'coordinates': [long, lat], 'properties': d})
        return HttpResponse(geojson.dumps(gj), content_type="application/json; charset='utf-8'")

