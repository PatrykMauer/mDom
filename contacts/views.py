from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacts
from django.core.mail import send_mail

def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing =request.POST['listing']
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        message =request.POST['message']
        user_id =request.POST['user_id']
        realtor_email =request.POST['realtor_email']

        # check if user has made inquiry already

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted=Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
           # if has_contacted:
                #messages.error(request, 'Twoje zapytanie dotyczące tej nieruchomości zostało już wysłane, wkrótce się z Tobą skontaktujemy.')
               # return redirect('/listings/'+listing_id)

        contact=Contacts(listing=listing, listing_id=listing_id, name=name, email=email,phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send mail

        send_mail (
                'Zapytanie dotyczące nieruchomości',
                name + ' zapytał o nieruchomość:' + listing + '. Treść wiadomości:'+ message + 
                'tel:' + phone,
                'mdom.zapytanie@gmail.com',
                [realtor_email],
                fail_silently=False
        )

        messages.success(request, 'Twoje zapytanie zostało wysłane, wkrótce się z Tobą skontaktujemy')
        return redirect('/listings/'+listing_id)


# Create your views here.
