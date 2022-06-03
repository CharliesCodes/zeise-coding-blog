from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('register/', views.UserRegisterView.as_view(), name='register'),
    path("edit-settings/", views.UserEditView.as_view(), name="edit_profile"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/change-password.html'), name='change_password'),
    path(
        "password/",
        views.PasswordsChangeView.as_view(
            template_name="registration/change-password.html"
        ),
        name="change_password",
    ),
    path("password-success", views.password_success, name="password_success"),
    path(
        "<int:pk>/profile/",
        views.ShowProfilePageView.as_view(),
        name="show_profile_page",
    ),
    path(
        "<int:pk>/edit-profile/",
        views.EditProfilePageView.as_view(),
        name="edit_profile_page",
    ),
    path(
        "create-profile/",
        views.CreateProfilePageView.as_view(),
        name="create_profile_page",
    ),
]
