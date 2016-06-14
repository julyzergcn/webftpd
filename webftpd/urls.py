
from django.conf.urls import url, include
from django.contrib import admin
from filebrowser.sites import site

urlpatterns = [
    url(r'^admin/fb/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
]
