from django.shortcuts import render, redirect 
from .models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            first_name = request.POST['firstName'],
            last_name = request.POST['lastName'],
            phone_number = request.POST['phoneNumber'],
            email = request.POST['email'],
            # role = request.POST['roleUser']
        )
        new_contact.save()
        return redirect('/')

    return render(request, 'personInfo.html')

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

