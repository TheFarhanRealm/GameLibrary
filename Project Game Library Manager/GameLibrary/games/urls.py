from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('new/', views.game_create, name='game_create'),
    path('edit/<int:pk>/', views.game_update, name='game_update'),
    path('delete/<int:pk>/', views.game_delete, name='game_delete'),
]