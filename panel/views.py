from django.views.generic import ListView, CreateView
from panel.models import Homework, Contact
from panel.forms import ContactForm


class HomeWorkView(ListView):
    model = Homework
    context_object_name = "homeworks"
    template_name = "studentspanel/index.html"


class ContactView(CreateView):
    success_url = '/panel/contact'
    model = Contact
    form_class = ContactForm
    template_name = "studentspanel/contact.html"
