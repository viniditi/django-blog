from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("about", views.about),
    path('<int:sla>', views.detail, name='detail'),
    path('<int:sla>/<int:algo>', views.detail, name='detail'),
]
