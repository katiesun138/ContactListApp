from typing import Optional
from django.shortcuts import render, redirect 
from .models import Contact
from django.views import generic
from django.views.generic.list import ListView
from .forms import AddForm



class indexView(ListView):
    model = Contact
    template_name: "index.html"

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

#function that allows me to add person's information
def addContact(request):
    form = AddForm()

    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/viewAll')

    context = {'form': form}
    return render(request, 'personInfo.html', context)


def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.first_name = request.POST['firstName']
        contact.last_name = request.POST['lastName']
        contact.phone_number = request.POST['phoneNumber']
        contact.email = request.POST['email']
        contact.save()

        return redirect('/')
    return render(request, 'personEdit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return redirect('/')
    #return render(request, 'index.html')

