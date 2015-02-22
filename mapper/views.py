from django.shortcuts import render
from django.views.generic import TemplateView




class MainPage(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request,'index.html')


