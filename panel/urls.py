from django.urls import path
from . import views

app_name = 'panel'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_user/', views.add_users, name='add_users'),
    path('user_dashboard/', views.users_dashboard, name='users_dashboard'),
    path('user_dashboard/<int:id>', views.delete_user, name='delete_user'),
    path('user_dashboard/<int:id>', views.edit_user, name='edit_user'),
]
