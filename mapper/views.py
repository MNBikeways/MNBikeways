from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
import overpass
import geojson


class MainPage(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request,'index.html')




class OverpassApiAjax(View):

    def get(self,request,*args,**kwargs):
        api = overpass.API()
        around = str(request.GET.get('around', '2500'))
        LatLonString = str(request.GET.get('lat', '42')) + "," + str(request.GET.get('lon', '-92')) + ")"
        r = api.Get('way(around:' + around + ',' + LatLonString + "[bicycle=yes]", asGeoJSON=True)
        return HttpResponse(geojson.dumps(r), content_type="application/json; charset='utf-8'")