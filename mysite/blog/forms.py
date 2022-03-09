from django import forms
from .models import Post, Category


# maybe make this a list in future if errors appear
category_choices = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'category', 'content', 'snippet', 'status', 'header_image') #'content_upload', 

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'author_field_id', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = category_choices, attrs={'class': 'form-control'}),
            # 'content': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'category', 'content', 'snippet', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # 'content': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }