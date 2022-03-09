from django import forms
from .models import Post, Category
from django.db import models


# maybe make this a list in future if errors appear
category_choices = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'content', 'snippet', 'status', 'header_image', 'pin') #'content_upload',

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'slug': models.SlugField(max_length=200, unique=True),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'author_field_id', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = category_choices, attrs={'class': 'form-control'}),
            # 'content': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        pin= forms.BooleanField(),


class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'category', 'content', 'snippet', 'status')
        slug = models.SlugField(max_length=200, unique=True)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # 'content': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }