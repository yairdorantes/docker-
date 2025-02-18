from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import Test
urlpatterns = [
    path("", csrf_exempt(Test.as_view()),name="xd"),
]