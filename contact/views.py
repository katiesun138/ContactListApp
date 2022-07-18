from multiprocessing import context
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
        if form.is_valid():
            print("form is REALL VALID")
            form.save()
            return redirect('/viewAll')
    context = {'form': form}
    return render(request, 'personInfo.html', context)


def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    form = AddForm(instance=contact)
    
    if request.method == 'POST':
        form = AddForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/viewAll')
    return render(request, 'personEdit.html', {'form': form})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return redirect('/viewAll')
    #return render(request, 'index.html')

