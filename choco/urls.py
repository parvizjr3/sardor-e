from django.urls import path
from . import views  # Import your views from views.py
from .views import IndexView, AboutView, ProductListView, ContactView, TestimonialView, ThankYouView, FastContactView, ProductDetailView, CustomLoginView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Class-based views
    path('', IndexView.as_view(), name='index_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('chocolate/', ProductListView.as_view(), name='chocolate_page'),  # Products page
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial_page'),
    path('thank-you/', ThankYouView.as_view(), name='thank_you'),
    path('fast-contact/', FastContactView.as_view(), name='fast_contact_page'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Custom Login View (CBV)
    path('login/', CustomLoginView.as_view(), name='login'),

    # Function-based views
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard view
    path('logout/', views.custom_logout, name='logout'),  # Logout view

    # You can add any other necessary URLs...
]

# Serve media files during development (only necessary in DEBUG mode)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
