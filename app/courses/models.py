from django.template.defaultfilters import slugify

from django.db import models
from django.contrib.auth.models import User
from blog.models import Category, Image
from ckeditor.fields import RichTextField


STATUS = ((0, "Draft"), (1, "Publish"))


class Course(models.Model):
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=120, blank=True)
    # slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="courses", null=True)
    categories = models.ManyToManyField(Category, related_name="courses")
    thumbnail = models.OneToOneField(Image, on_delete=models.SET_NULL, related_name="courses", null=True, blank=True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    snippet = models.CharField(max_length=200)
    pin = models.BooleanField(default=False)

    # price
    # external_link

    class Meta:
        ordering = ["title"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title