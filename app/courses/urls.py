from re import template
from django.urls import path
from . import views

urlpatterns = [
    path("", views.CourseList.as_view(), name="courses-home"),
    path("kategorie/<str:category>/", views.category_view, name="course-category"),
    # path("<slug:slug>/", views.PostDetail.as_view(), name="course-detail"),
]
