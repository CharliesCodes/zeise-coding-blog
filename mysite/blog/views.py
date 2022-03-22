from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q


class PostList(ListView):
    queryset = Post.objects.filter(status=1, pin=False).order_by('-created_on')
    template_name = 'blog_home.html'

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        pinned_posts = Post.objects.filter(pin=True)
        context = super(PostList, self).get_context_data(*args, **kwargs)

        context['categories_menu'] = categories_menu
        context['pinned_posts'] = pinned_posts
        return context

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


def category_view(request, category):
    category_name = category.replace('-',' ')
    category_posts = Post.objects.filter(category=category_name)
    return render(request, 'categories.html', {'category': category_name, 'category_posts': category_posts})


def search_post(request):
    if request.method == "POST":
        search = request.POST['post-search-input']
        filtered_posts = Post.objects.filter(
            Q(title__contains=search) | Q(snippet__contains=search) | Q(content__contains=search) |
            Q(category__contains=search)) # Q(content_upload__contains=search) |
        return render(request, 'search_post.html', {'search': search, 'filtered_posts': filtered_posts})
    else:
        return render(request, 'search_post.html', {})

def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', arg=[str(post.id)]))
