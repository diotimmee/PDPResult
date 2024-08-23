from django.views.generic import ListView, TemplateView
from edu.models import Lesson


class EduView(ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = "edu/It.html"


class ClassView(TemplateView):
    template_name = "edu/class.html"


# testcase

class HomeIn(TemplateView):
    template_name = "testcase/index.html"


class TestEng(TemplateView):
    template_name = "testcase/test.html"


class BeginnerView(TemplateView):
    template_name = "OnlineDarslar/begginer.html"


class IntermediateView(TemplateView):
    template_name = "OnlineDarslar/intermediate.html"


class ElementaryView(TemplateView):
    template_name = "OnlineDarslar/elementary.html"


class Pre_intermediateView(TemplateView):
    template_name = "OnlineDarslar/preintermediate.html"
