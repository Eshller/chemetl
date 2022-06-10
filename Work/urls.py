from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.index) ,
    path('projects/<int:id>' , views.about) ,
    path('equipment/<int:id>' , views.comp)
]
