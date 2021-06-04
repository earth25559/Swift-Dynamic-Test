from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('fill-info/', views.fill_info, name='fill_info'),
    path('success/', views.send_mail, name='send_mail'),
    path('view-user/', views.view_user, name='view_user'),
    path('delete-user/<str:pk>/', views.delete_user, name='delete_user'),
    path('pre-fill', views.pre_fill, name='pre_fill'),
]
