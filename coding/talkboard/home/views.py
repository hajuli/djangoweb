# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response
from favorites import models as models_fv

def index(request):
    fvs = models_fv.get_all_favorites()
    datas = []
    i = fvs.count() - 1
    co = 0
    while i >= 0:
        e = {}
        e["index"] = unicode(co % 6)
        e["value"] = fvs[i]
        datas.append(e)
        # print co, e['value'].label_name
        i -= 1
        co += 1
    return render_to_response("home.html", {"datas": datas})

def main():
    index("xx")
    
if "__main__" == __name__:
    main()
