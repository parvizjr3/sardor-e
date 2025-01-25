from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)  # Field for the contact's name
    phone_number = models.CharField(max_length=255)  # Field for phone number without limits
    message = models.TextField()  # Field for the message with no length restriction

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Aloqalar"




class FastContact(models.Model):
    phone_number = models.CharField(max_length=255)  # Field for phone number with no restrictions

    def __str__(self):
        return self.phone_number
    
    class Meta:
        verbose_name_plural = "Tez aloqa"



class Product(models.Model):
    photo = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    info = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Mahsulot"



class Testimonial(models.Model):
    
    photo = models.ImageField(upload_to='testimonials_photos/')
    name = models.CharField(max_length=100)
    quote = models.TextField()

    def __str__(self):
        return f"Fikr  {self.name}   tomonidan"
    
    class Meta:
        verbose_name_plural = "Fikrlar"
    
    
