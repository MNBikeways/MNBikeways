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
        r = api.Get('way(around:1000,' + str(request.GET.get('lat', '42')) + "," + str(
            request.GET.get('lon', '-92')) + ")" + "[bicycle=yes];")
        print(r['elements'])
        return HttpResponse(geojson.dumps(geojson.loads(str(r['elements']), encoding=None)),
                            content_type="application/json; charset='utf-8'")