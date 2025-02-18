from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

# Create your views here.
class Test(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"message":"oki lalaalalalaal yooooooooo!!!"})
        