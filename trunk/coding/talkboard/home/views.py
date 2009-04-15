# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response
from favorites import models as models_fv

def index(request):
    fvs = models_fv.get_all_favorites()
    datas = []
    i = 0
    for xx in fvs:
        e = {}
        e["index"] = unicode(i % 6)
        e["value"] = xx
        datas.append(e)
        i += 1
    return render_to_response("home.html", {"datas": datas})