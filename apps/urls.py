from django.urls import path
from .views import HomeView, AboutView, TestView, TestOneView, TestTowView, TestThereView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('tests', TestView.as_view(), name='test'),
    path('testone', TestOneView.as_view(), name='testone'),
    path('test_two', TestTowView.as_view(), name='test_tow'),
    path('test_there', TestThereView.as_view(), name='test_there'),

]
