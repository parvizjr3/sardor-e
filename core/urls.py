from django.contrib import admin
from django.urls import path

# includ ni chaqirdik
from django.urls import path, include

# bu if debugniki
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('choco.urls')),
]


handler404 = 'choco.views.custom_404_view'

 

#Bu kod bloklari Django’da DEBUG rejimi faolligida statik va media fayllarni xizmat ko'rsatish uchun kerak. Keling, har birini tushuntirib beram
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
