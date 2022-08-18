from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'impressum', 'data_security', 'blog-home', 'courses-home']

    def location(self, item):
        return reverse(item)