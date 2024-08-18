from django.urls import path
from panel.views import HomeWorkView, ContactView

urlpatterns = [
    path('', HomeWorkView.as_view(), name='homework'),
    path('contact', ContactView.as_view(), name='contact'),

]
