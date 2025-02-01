from django.contrib import admin
from django.urls import path

from django.conf.urls import handler404

# includ ni chaqirdik
from django.urls import path, include

# bu if debugniki
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('choco.urls')),
]





handler404 = 'core.views.page_not_found'
 

#Bu kod bloklari Django’da DEBUG rejimi faolligida statik va media fayllarni xizmat ko'rsatish uchun kerak. Keling, har birini tushuntirib beram
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
