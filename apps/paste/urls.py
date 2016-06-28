"""pastely URL Configuration
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/paste/view/(?P<paste_id>[A-Za-z0-9]{8})$', views.ViewPaste.as_view()),
    url(r'^api/v1/paste/create$', views.CreatePaste.as_view())
]
