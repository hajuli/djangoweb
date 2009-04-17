# Create your views here.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import favorites.models as fvs_md

def index(request):
    fvs = fvs_md.get_all_favorites()
    return render_to_response(r"favorites/add_favorites.html", {"fvs": fvs})


def save_favorites(request):
    favorite = fvs_md.Favorite()
    favorite.label_name = request.POST.get('label_name', "null").decode("utf-8")
    favorite.url_path = request.POST.get('url_path', "null").decode("utf-8")
    favorite.put()
    return HttpResponseRedirect('/')

def delete_favorites(request):
    label_name = request.GET.get('label_name', "").decode("utf-8")
    if label_name:
        fvs_md.delele_favorites(label_name)
    return HttpResponseRedirect('/')

def main():
    pass

if __name__ == '__main__':
    main()

