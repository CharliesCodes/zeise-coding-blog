from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page_view, name="home"),
    path("about/", views.about_page_view, name="about"),
    path("impressum/", views.impressum_page_view, name="impressum"),
    path("datenschutzerklaerung/", views.data_security_view, name="data_security"),
]
