from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticViewSitemap
from blog.sitemaps import PostSitemap
from courses.sitemaps import CourseSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "posts": PostSitemap,
    # 'courses': CourseSitemap,
}

urlpatterns = [
    path("", include("home.urls")),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("kurse/", include("courses.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("robots.txt", include("robots.urls")),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    re_path("djga/", include("google_analytics.urls")),
    path(
        "favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
