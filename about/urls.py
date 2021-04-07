from django.urls import path
from about import views

urlpatterns = [
    path('', views.show_about)
]