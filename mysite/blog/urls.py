from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog-home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
    path('add-post', views.AddPostView.as_view(), name='add-post'),
    path('edit-post/<slug:slug>', views.EditPostView.as_view(), name='edit-post'),
    path('delete-post/<slug:slug>', views.DeletePostView.as_view(), name='delete-post'),
    path('add-category', views.AddCategoryView.as_view(), name='add-category'),
    path('category/<str:category>/', views.category_view, name='category'),
    path('like/<slug:slug>/', views.like_view, name='like-post'),
    path('search_post', views.search_post, name='search-post'),
]
