from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^uploads/', include('uploads.urls', namespace="uploads")),
    url(r'^mobile_upload/', include('mobile_upload.urls', namespace="mobile_upload")),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
