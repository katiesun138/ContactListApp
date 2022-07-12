from django.shortcuts import render, redirect 
from .models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html')

def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            first_name = request.POST['firstName'],
            last_name = request.POST['lastName'],
            phone_number = request.POST['phoneNumber'],
            email = request.POST['email']
        )
        new_contact.save()
        return redirect('/')

    return render(request, 'personInfo.html')