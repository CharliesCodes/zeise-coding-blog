from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount


STATUS = ((0, "Draft"), (1, "Publish"))


class Image(models.Model):
    image = CloudinaryField("image")


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog-home")


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="author", null=True
    )
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(blank=True, max_length=155)
    categories = models.ManyToManyField(Category, related_name="posts")
    header_image = models.ImageField(blank=True, null=True, upload_to="images/")
    header_image_alt = models.CharField(blank=True, null=True, max_length=400)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, default=None, blank=True, related_name="posts")
    snippet = models.CharField(default=None, blank=True, max_length=200)
    pin = models.BooleanField(default=False)
    vg_wort_counter = models.CharField(blank=True, max_length=500)
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )

    def current_hit_count(self):
        return self.hit_count.hits

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-home")


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.post.title, self.name)
