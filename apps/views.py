from django.views.generic import TemplateView, ListView
from apps.models import About


class HomeView(TemplateView):
    template_name = "Asosiy/index.html"


class AboutView(ListView):
    model = About
    context_object_name = "posts"
    template_name = "Haqidalar/Haqida.html"


class TestView(TemplateView):
    template_name = "Asosiy/indexs.html"


class TestOneView(TemplateView):
    template_name = "Asosiy/TestOne.html"


class TestTowView(TemplateView):
    template_name = "Asosiy/TestTwo.html"


class TestThereView(TemplateView):
    template_name = "Asosiy/TestThere.html"
