from django.urls import path
from . import views


urlpatterns = [
    path('', views.gifts, name='gifts'),
    path('add/gift/<str:user>/', views.add_gift, name='add_gift'),
    path('view/<str:user>/<str:id>', views.view_gift, name='view_gift'),
]
