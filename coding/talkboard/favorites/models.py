# -*- coding: UTF-8 -*-

from django.db import models
from google.appengine.ext import db

# Create your models here.

class Favorite(db.Model):
    author = db.UserProperty()
    label_name = db.StringProperty(multiline=False)
    url_path = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    
    
def get_all_favorites():
    fvs = []
    try:
        fvs = db.GqlQuery("SELECT * "
                                "FROM Favorite "
                                "ORDER BY label_name DESC LIMIT 100")
    except :
        print "gqlQuery exception"
    return fvs


def delele_favorites(label_name):
    fvs = get_all_favorites()
    for fv in fvs:
        if (label_name == fv.label_name):
            db.delete(fv)
    pass