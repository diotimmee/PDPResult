from django.urls import path
from .views import HomeView, SinfView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', SinfView.as_view(), name='Sinf.html'),
]
