from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.urls import reverse

class BlogFeed(Feed):
    title = "Latest Post"
    link = "/blog/"
    description = "Latest blog posts"

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.snippet, 60)