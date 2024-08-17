from django.views.generic import ListView
from panel.models import Homework


class HomeWorkView(ListView):
    model = Homework
    context_object_name = "homeworks"
    template_name = "studentspanel/index.html"
