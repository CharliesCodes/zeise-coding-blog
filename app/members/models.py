from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = RichTextUploadingField(blank=True, null=True)
    snippet = RichTextUploadingField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=200, blank=True, null=True)
    github_url = models.CharField(max_length=200, blank=True, null=True)
    linkedin_url = models.CharField(max_length=200, blank=True, null=True)
    reddit_url = models.CharField(max_length=200, blank=True, null=True)
    instagram_url = models.CharField(max_length=200, blank=True, null=True)
    pinterest_url = models.CharField(max_length=200, blank=True, null=True)
    twitter_url = models.CharField(max_length=200, blank=True, null=True)
    facebook_url = models.CharField(max_length=200, blank=True, null=True)
    # social_media = [website_url, github_url, linkedin_url, reddit_url, instagram_url,pinterest_url, twitter_url, facebook_url]

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("home")
