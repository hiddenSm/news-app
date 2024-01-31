from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_news, name='news'),
    path("/<int:pk>", views.show_news_detail, name='news_detail'),
    path("like/<int:pk>", views.like_news, name='news_like'),
    path("create/", views.create_news, name='news_create'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]