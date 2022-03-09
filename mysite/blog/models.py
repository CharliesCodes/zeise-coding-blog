from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True, null=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=200, blank=True, null=True)
    github_url = models.CharField(max_length=200, blank=True, null=True)
    linkedin_url = models.CharField(max_length=200, blank=True, null=True)
    reddit_url = models.CharField(max_length=200, blank=True, null=True)
    instagram_url = models.CharField(max_length=200, blank=True, null=True)
    pinterest_url = models.CharField(max_length=200, blank=True, null=True)
    twitter_url = models.CharField(max_length=200, blank=True, null=True)
    facebook_url = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')



STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-home')


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=200, default="Coding")
    header_image=models.ImageField(blank=True, null=True, upload_to="images/")
    content = RichTextField(blank=True, null=True)
    content_upload = RichTextUploadingField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    snippet = models.CharField(max_length=200)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


