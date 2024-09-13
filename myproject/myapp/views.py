from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def myview(request): #permission denied if anonymous user
    if request.user.is_anonymous():
        raise PermissionDenied()
    
@login_required #only allows access for logged users
def myview(request):
    return HttpResponse("Hello World")

def testpermission(user):
    if user.is_authenticated() and user.has_perm("myapp.change_category"):
        return True
    else:
        return False