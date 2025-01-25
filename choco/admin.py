from django.contrib import admin


from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'message')  # Columns to display in the admin list view
    search_fields = ('name', 'phone_number')  # Searchable fields


from .models import FastContact

@admin.register(FastContact)
class FastContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)


from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'info', 'photo')
    search_fields = ('name', 'info')

admin.site.register(Product, ProductAdmin)




from django.contrib import admin
from .models import Testimonial

admin.site.register(Testimonial)
