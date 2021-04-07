from django.urls import path
from contacts import views

urlpatterns = [
    path('', views.show_contacts, name='contacts')
]