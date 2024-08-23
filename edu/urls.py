from django.urls import path
from edu.views import EduView, ClassView, HomeIn, TestEng, BeginnerView, IntermediateView, ElementaryView, \
    Pre_intermediateView

urlpatterns = [
    path('', EduView.as_view(), name='edu'),
    path('class', ClassView.as_view(), name='class'),
    path('home', HomeIn.as_view(), name='home'),
    path('test', TestEng.as_view(), name='test'),
    path('beginner', BeginnerView.as_view(), name='beginner'),
    path('intermediate', IntermediateView.as_view(), name='intermediate'),
    path('elementary', ElementaryView.as_view(), name='elementary'),
    path('pre', Pre_intermediateView.as_view(), name='pre'),
]
