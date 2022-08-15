from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.db.models import Q

from blog.models import Category, Image
from .models import Course


class CourseList(ListView):
    queryset = Course.objects.filter(status=1, pin=False).order_by("-created_on")
    template_name = "courses_home.html"

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        pinned_courses = Course.objects.filter(pin=True)
        context = super(CourseList, self).get_context_data(*args, **kwargs)

        context["categories_menu"] = categories_menu
        context["pinned_courses"] = pinned_courses

        return context


def category_view(request, category):
    category_name = category.replace("-", " ")
    category_posts = Course.objects.filter(Q(categories__name__icontains=category_name))
    return render(
        request,
        "categories.html",
        {"category": category_name, "category_posts": category_posts},
    )