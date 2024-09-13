from django.shortcuts import render
from django.core.exceptions import PermissionDenied

# Create your views here.

def myview(request):
    if request.user.is_anonymous():
        raise PermissionDenied()