from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prihlasenie/', views.prihlasenie, name='prihlasenie'),
    path('home/',views.home, name='home'),
    path('odhlasenie/', views.odhlasenie, name='odhlasenie'),
    path('cvicenie/<int:cvicenie_id>/', views.cvicenie, name='cvicenie')
]