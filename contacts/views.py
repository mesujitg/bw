from django.shortcuts import render
from contacts.models import Contact


def show_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})
