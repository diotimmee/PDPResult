from django.urls import path
from panel.views import HomeWorkView, ContactView, RegisterView, LoginViews

urlpatterns = [
    path('', HomeWorkView.as_view(), name='homework'),
    path('contact', ContactView.as_view(), name='contact'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginViews.as_view(), name='login'),

]
