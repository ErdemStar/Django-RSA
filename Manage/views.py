# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from sifrele import RSA


def Yonlendir(request):
    return HttpResponseRedirect("Anasayfa")

def Anasayfa(request):
    if request.method == "GET":
        return render(request,"Anasayfa.html",{"method":"GET"})
    elif request.method == "POST":
        text = request.POST["text"]
        rsa = RSA()
        tut = rsa.SifreYap(text)
        tut2 = rsa.SifreKir()
        return render(request,"Anasayfa.html",{"al":tut , "al2":tut2,"method":"POST"})
