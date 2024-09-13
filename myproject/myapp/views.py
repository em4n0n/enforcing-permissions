from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def myview(request):
    if request.user.is_anonymous():
        raise PermissionDenied()
    
@login_required
def myview(request):
    return HttpResponse("Hello World")