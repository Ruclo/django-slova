from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'cvicenia', views.CvicenieView.as_view())#CvicenieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cvicenia/', views.CvicenieView.as_view()),
    path('pokusy/', views.PokusView.as_view())
]