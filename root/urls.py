from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from root.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT, DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path('edu/', include('edu.urls'))
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)