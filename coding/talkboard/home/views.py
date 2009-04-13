# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response
from favorites import models

def index(request):
    fvs = models.get_all_favorites()
    return render_to_response("home.html", {"fvs": fvs})