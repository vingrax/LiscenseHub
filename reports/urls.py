from django.urls import path
from . import views

urlpatterns = [
    path('general/',views.generalView,name='general'),
    #path('general/',views.testView,name='general')
    ]