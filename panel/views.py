from panel.forms import ContactForm
from django.urls import reverse_lazy
from panel.models import Homework, Contact
from panel.forms import SignupForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView


class HomeWorkView(ListView):
    model = Homework
    context_object_name = "homeworks"
    template_name = "studentspanel/index.html"


class ContactView(CreateView):
    success_url = '/panel/contact'
    model = Contact
    form_class = ContactForm
    template_name = "studentspanel/contact.html"


class RegisterView(FormView):
    template_name = 'studentspanel/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginViews(FormView):
    template_name = 'studentspanel/signin.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)
