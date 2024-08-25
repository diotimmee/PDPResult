from django.urls import path
from panel.views import (HomeWorkView, ContactView, RegisterView, LoginViews, ProfileView, BeginnerView,
                         IntermediateView, ElementaryView,
                         Pre_intermediateView)

urlpatterns = [
    path('', HomeWorkView.as_view(), name='homework'),
    path('contact', ContactView.as_view(), name='contact'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginViews.as_view(), name='login'),
    path('profileview', ProfileView.as_view(), name='profile_view'),
    path('beginner', BeginnerView.as_view(), name='beginner'),
    path('intermediate', IntermediateView.as_view(), name='intermediate'),
    path('elementary', ElementaryView.as_view(), name='elementary'),
    path('pre', Pre_intermediateView.as_view(), name='pre'),

]
