from django.urls import path
from .views import EduView, ClassView, HomeIn, TestEng

urlpatterns = [
    path('', EduView.as_view(), name='edu'),
    path('class', ClassView.as_view(), name='class'),
    path('home', HomeIn.as_view(), name='home'),
    path('test', TestEng.as_view(), name='test'),
]
