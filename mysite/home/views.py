from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from members.models import Profile
from django.shortcuts import render
class HomePageView(TemplateView):
    template_name = 'home.html'

def about_page_view(request):
    admin_profile = get_object_or_404(Profile, id=1)
    return render(request, 'about.html', {'admin_profile':admin_profile})