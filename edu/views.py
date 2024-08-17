from django.views.generic import ListView, TemplateView
from edu.models import Lesson


class EduView(ListView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = "edu/It.html"


class ClassView(TemplateView):
    template_name = "edu/class.html"
