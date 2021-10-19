from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('request', views.request_form, name='request'),
]