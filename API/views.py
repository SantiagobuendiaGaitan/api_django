from tkinter import image_names
from django.shortcuts import render
from django.views import View
from .models import Biblioteca
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

# Create your views here.
class BibliotecaListView(View):
    def get(self, request):
        if('nombre' in request.GET):
            bList = Biblioteca.objects.filter(nombre__contains=request.GET['nombre'])
        else: 
            bList = Biblioteca.objects.all()
        return JsonResponse(list(bList.values()), safe = False)



class BibliotecaDetailView(View):
    def get(self, request, pk):
        dList = Biblioteca.objects.get(pk=pk)
        return JsonResponse(model_to_dict(dList))
        
