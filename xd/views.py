from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

# Create your views here.
class Test(View):
    def get(self, request, *args, **kwargs):
        print("woooooaaaaa im a fucking crack wow!")
        return JsonResponse({"message":"hello world fellas!!!","status":200})
        