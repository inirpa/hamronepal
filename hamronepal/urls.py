from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = 'हाम्रो नेपाल - Ramro Nepal'
admin.site.site_title = 'Hamro Nepal Admin'

urlpatterns = [
	url(r'^$', include('home.urls')),
	url(r'^memo/', include('memo.urls')),
	url(r'^unescosites/', include('unescosites.urls')),
	
    url(r'^admin/', admin.site.urls),
]


urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)