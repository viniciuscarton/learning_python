from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('basic/', views.basic_view),
    path('intermediate/', views.intermediate_view),
    path('advanced/', views.advanced_view),
    path('<str:heading>/fun/', views.file_view_fun),
    path('<str:heading>/utility/', views.file_view_utility),
]


