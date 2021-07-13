from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def home(request):
    return JsonResponse({"HELLO": "WORLD!"})


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]
