from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy



class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_home.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'