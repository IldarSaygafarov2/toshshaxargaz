from django.urls import path

from . import views


urlpatterns = [
    # path('all/', views.get_all_users),
    path('login/', views.user_login),
]
