from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views as hello
from django.conf import settings
from django.conf.urls.static import static

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", include('hello.urls'), name="index"),
    path('markdownx/', include('markdownx.urls')),
    path("db/", hello.db, name="db"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
