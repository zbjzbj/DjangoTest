from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def tem(request):
    return render(request, "tmp.html", {"name": "小明"})
