from django.urls import path
from panel.views import HomeWorkView

urlpatterns = [
    path('', HomeWorkView.as_view(), name='homework'),

]
