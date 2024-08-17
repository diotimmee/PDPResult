from django.urls import path
from .views import EduView, ClassView

urlpatterns = [
    path('', EduView.as_view(), name='edu'),
    path('class/', ClassView.as_view(), name='class'),
]
