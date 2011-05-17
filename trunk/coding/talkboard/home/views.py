# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response
from favorites import models as models_fv

def index(request):
    fvs = models_fv.get_all_favorites()
    datas = []
    ct = fvs.count()
    co = 0
    i = 0
    while i < ct:
        e = {}
        e["index"] = unicode(co % 6)
        e["value"] = fvs[i]
        f = fvs[i]
        i = i + 1
        if 1 == f.deleted:
            continue
        
        datas.append(e)
        # f =fvs[i]
        # print co, f.label_name, f.deleted, "<hr/>"

        co = co + 1
    return render_to_response("home.html", {"datas": datas})

def main():
    index("xx")
    
if "__main__" == __name__:
    main()
