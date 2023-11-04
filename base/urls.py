from django.urls import path
from . import views

urlpatterns = [
    # user
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/<str:pk>', views.userProfile, name='profile'),

    # home
    path('', views.home, name='home'),

    # room
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),

    # comments
    path('delete-comment/<str:pk>/', views.deleteComment, name='delete-comment'),

]
