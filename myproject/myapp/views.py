from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

# Create your views here.

# def myview(request): #permission denied if anonymous user
#     if request.user.is_anonymous():
#         raise PermissionDenied()
    
# @login_required #only allows access for logged users
# def myview(request):
#     return HttpResponse("Hello World")

# def testpermission(user): # returns true if if user is authenticated
#     if user.is_authenticated() and user.has_perm("myapp.change_category"):
#         return True
#     else:
#         return False

# @user_passes_test(testpermission)
# def change_ctg(request):

# @permission_required("myapp.change_category")
# def store_creator(request):

from .models import Product

class ProductListView(PermissionRequiredMixin, ListView):
    permission_required = "myapp.view_product"
    template_name = "product.html"
    model = Product