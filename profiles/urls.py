from django.urls import path
from . import views


urlpatterns = [
    path('<str:user>/', views.profile, name='profile'),
    path('edit_profile/<str:user>',
         views.edit_profile, name='edit_profile'),
    path('edit_address/<str:user>',
         views.edit_address, name='edit_address'),
]
