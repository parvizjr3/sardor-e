from django.shortcuts import render

from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import FastContactForm

# templateview chaqirildi
from django.views.generic import TemplateView


################################################3
from django.views.generic import TemplateView
from .models import Product, Testimonial

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()  # Add all products to context
        context['testimonials'] = Testimonial.objects.all()  # Add all testimonials to context
        return context



##############################################
class AboutView(TemplateView):
    template_name = 'about.html'





#################################################
class ChocolateView(TemplateView):
    template_name = 'chocolate.html'

##################################################
class ThankYouView(TemplateView):
    template_name = 'thank_you.html'




#################################################
from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'contact.html'  # Template for the contact form
    form_class = ContactForm  # Use the form you created in forms.py
    success_url = '/thank-you/'  # Redirect URL after successful submission

    def form_valid(self, form):
        # Save the form data to the database
        form.save()
        return super().form_valid(form)




###################################################
from django.views.generic import TemplateView
from .models import Testimonial

class TestimonialView(TemplateView):
    template_name = 'testimonial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all()  # Get all testimonials
        return context


#############################################



from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import FastContactForm
from .models import FastContact

class FastContactView(FormView):
    template_name = 'contact.html'  # The template containing the form
    form_class = FastContactForm  # The form class for fast contact
    success_url = reverse_lazy('thank_you')  # Redirect after successful submission

    def form_valid(self, form):
        form.save()  # Save the data to the database
        return super().form_valid(form)
    

########################################################################


from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'chocolate.html'  # Correct template path
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#############################################################################



from django.views.generic import DetailView
from .models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'  # Template for the product detail page
    context_object_name = 'product'



##############################################################################


from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'login.html'  # Path to your custom login template
    success_url = reverse_lazy('dashboard')  # Redirect to dashboard after successful login




# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')  # your dashboard template

# Custom Logout View
def custom_logout(request):
    logout(request)  # This will log the user out
    return redirect('index_page')  # Redirect to the homepage or any other page you want




from django.http import HttpResponseNotFound
from django.template.loader import render_to_string
from django.conf import settings

def custom_404_view(request, exception):
    response = render_to_string('404.html', {})
    return HttpResponseNotFound(response)

