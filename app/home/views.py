from django.shortcuts import get_object_or_404

# from django.views.generic import TemplateView
from members.models import Profile
from django.shortcuts import render
import cloudinary

# class HomePageView(TemplateView):
#     template_name = 'home.html'


def home_page_view(request):
    return render(request, "home.html")


def about_page_view(request):
    admin_profile = get_object_or_404(Profile, id=1)
    return render(request, "about.html", {"admin_profile": admin_profile})


def impressum_page_view(request):
    return render(request, "impressum.html")


def data_security_view(request):
    return render(request, "data_protection.html")