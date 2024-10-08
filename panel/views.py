from panel.forms import ContactForm
from django.urls import reverse_lazy
from panel.models import Homework, Contact, Pre, Intermediate, Beginner, Elementary
from panel.forms import SignupForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, TemplateView


class ProfileView(TemplateView):
    template_name = "EditProfile.html"


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


class BeginnerView(ListView):
    model = Beginner
    context_object_name = "beginners"
    template_name = "OnlineDarslar/begginer.html"


class IntermediateView(ListView):
    model = Intermediate
    context_object_name = "inters"

    template_name = "OnlineDarslar/intermediate.html"


class ElementaryView(ListView):
    model = Elementary
    context_object_name = "elements"

    template_name = "OnlineDarslar/elementary.html"


class Pre_intermediateView(ListView):
    model = Pre
    context_object_name = "pres"

    template_name = "OnlineDarslar/preintermediate.html"
