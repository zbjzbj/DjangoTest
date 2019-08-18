from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.

def tem(request):
    return render(request, "son-tmp.html", {"name": "小明"})
