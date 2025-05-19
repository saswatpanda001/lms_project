from django.contrib import admin
from django.urls import path,include

app_name = "teacher"



from django.http import HttpResponse
def basic_view(request):
    return HttpResponse("This is a basic response without HTML page.")

urlpatterns = [
    path('basic/', basic_view, name='basic'),
]
