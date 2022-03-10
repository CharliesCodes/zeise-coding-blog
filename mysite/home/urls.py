from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.about_page_view, name='about'),
]