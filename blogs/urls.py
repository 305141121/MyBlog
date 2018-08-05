from django.urls import path
from . import views

urlpatterns = [
    path(r"", views.index),
    path(r"submit", views.submit),
    path(r"page", views.pageItem)
]

