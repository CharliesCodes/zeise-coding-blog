from django import forms
from .models import Post, Category, Image
from django.db import models


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "author",
            "description",
            "content",
            "categories",
            "snippet",
            "status",
            "header_image",
            "header_image_alt",
            "pin",
            "vg_wort_counter",
        )
        slug = models.SlugField(max_length=200, unique=True)
        # images = Image
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "author_field_id",
                    "type": "hidden",
                }
            ),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "categories": forms.CheckboxSelectMultiple,
            # "header_image",
            # "header_image_alt",
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "vg_wort_counter": forms.Textarea(attrs={"class": "form-control"}),
        }
        pin = (forms.BooleanField(),)


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ("title", "slug", "description", "categories", "content", "snippet", "status", "header_image",
            "header_image_alt", "pin", "vg_wort_counter")
        slug = models.SlugField(max_length=200, unique=True)
        categories = forms.ModelMultipleChoiceField(
            queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "categories": forms.CheckboxSelectMultiple,
            # "header_image",
            # "header_image_alt",
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "vg_wort_counter": forms.Textarea(attrs={"class": "form-control"}),
        }
