from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.urls import reverse

# from django.utils.feedgenerator import Atom1Feed


class BlogFeed(Feed):
    title = "Latest Post"
    link = "/blog/"
    description = "Latest blog posts"
    # Create Atom Feed instead of RSS
    # feed_type = Atom1Feed

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.snippet, 60)
