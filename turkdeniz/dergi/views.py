from django.shortcuts import render
from django.http import HttpResponse


def anasayfa(request):
    return render(request,'dergi\index.html')

def hakkinda(request):
    return render(request,'dergi\hakkinda.html')

def amacvekapsam(request):
    return render(request,'dergi\\amacvekapsam.html')

def kunye(request):
    return render(request,'dergi\kunye.html')

def kurullar(request):
    return render(request,'dergi\kurullar.html')

def yayinpolistikasi(request):
    return render(request,'dergi\yayinpolitikasi.html')

def etik(request):
    return render(request,'dergi\etik.html')

def iletisim(request):
    return render(request,'dergi\iletisim.html')

# Create your views here.
