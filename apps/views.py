from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "Asosiy/index.html"


class AboutView(TemplateView):
    template_name = "Haqidalar/Haqida.html"


class TestView(TemplateView):
    template_name = "Asosiy/TestTurlari/index.html"


class TestOneView(TemplateView):
    template_name = "Asosiy/TestOne.html"


class TestTowView(TemplateView):
    template_name = "Asosiy/TestTwo.html"


class TestThereView(TemplateView):
    template_name = "Asosiy/TestThere.html"
