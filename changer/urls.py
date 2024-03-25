
from django.contrib import admin
from django.urls import path
from . import main


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('' , main.web , name="index"),
    path('' , main.home , name="home"),
    path('result' , main.result , name='result') 
]
