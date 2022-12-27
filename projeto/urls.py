from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def my_view(request):
    return HttpResponse('')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', my_view),
]
