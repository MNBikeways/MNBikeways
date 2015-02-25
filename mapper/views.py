from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
import overpass
import geojson



# helper function for Overpass API to output valid geojson
def osmJsonToGeoJson(data):
    for feat in data['elements']:
        for point in feat['nodes']:
            print(point)

class MainPage(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request,'index.html')




class OverpassApiAjax(View):

    def get(self,request,*args,**kwargs):
        api = overpass.API()
        # OSM EPSG is 900913
        LatLonString = str(request.GET.get('lat', '42')) + "," + str(request.GET.get('lon', '-92')) + ")"
        r = api.Get('way(around:2000,' + LatLonString + "[bicycle=yes]", asGeoJSON=True)

        print(r)

        return HttpResponse(geojson.dumps(r), content_type="application/json; charset='utf-8'")