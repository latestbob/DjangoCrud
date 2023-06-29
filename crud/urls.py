from django.urls import path

from . import views

urlpatterns = [
    #  all url relating to crud app

    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('details/<str:id>/', views.details, name='details'),
    path('pension/<str:id>/', views.deletePension, name="delete"),


]
