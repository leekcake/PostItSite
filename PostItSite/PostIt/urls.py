from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('post', views.post, name='post'),
    path('delete/<int:id>', views.delete, name='delete'),

    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup')
]