from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
import overpass



class MainPage(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request,'index.html')




class OverpassApiAjax(View):

    def get(self,request,*args,**kwargs):
        request