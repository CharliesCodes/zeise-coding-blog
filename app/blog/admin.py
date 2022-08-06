from django.contrib import admin
from .models import Post, Category, Comment, Picture


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_on") #"slug",
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Picture)
