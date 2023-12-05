from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp/list_contacts.html', {'contacts': contacts})

def add_contact(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Contact.objects.create(title=title, description=description)
        return redirect('list_contacts')
    return render(request, 'myapp/add_contact.html', {})

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        contact.title = title
        contact.description = description
        contact.save()
        return redirect('list_contacts')

    return render(request, 'myapp/edit_contact.html', {'contact': contact})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('list_contacts')