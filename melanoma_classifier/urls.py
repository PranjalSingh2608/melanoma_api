from django.urls import path
from .views import mainView
urlpatterns=[
    path('upload/', mainView, name = 'prediction'),
]