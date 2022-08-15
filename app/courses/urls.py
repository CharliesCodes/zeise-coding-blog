from re import template
from django.urls import path
from . import views

urlpatterns = [
    path("", views.CourseList.as_view(), name="courses-home"),
    # path("category/<str:category>/", views.category_view, name="category"),
    # path("<slug:slug>/", views.PostDetail.as_view(), name="post-detail"),

]
