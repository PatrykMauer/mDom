from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.

def index(request):
    return render(request, 'publish/publish.html')

def published(request):
    if request.method=='GET':
        return render(request, 'publish/publish.html')

    if request.method=='POST':
        listing =request.POST['listing']
        address =request.POST['address']
        city =request.POST['city']
        price =request.POST['price']
        bathrooms =request.POST['bathrooms']
        garage =request.POST['garage']
        sqft =request.POST['sqft']
        lot_size =request.POST['lot_size']
        name = request.POST['name']
        user_email =request.POST['email']
        phone =request.POST['phone']
        message =request.POST['message']

    
        # Send mail
        email = EmailMessage(
        'Zgłoszenie nieruchomości',
        name + ' zgłosił: ' + listing + '\nCena: ' + price + '\nMiasto: '
         + city +'\nAdres:' + address + '\nPowierzchnia: ' + sqft + '\nPiętro: '+ garage + '\nIlość pokoi: '+ bathrooms + '\nDziałka: ' + lot_size
        + '\nTel: ' + phone +'\nEmail: ' + user_email + '\nDodatkowa wiadomość: '+ message,
        'mdom.zapytanie@gmail.com',
        ['mdomkontakt@gmail.com'],)
        
        #if in FILES request
        photo_1 = request.FILES.get('photo_1', 0)
        if photo_1:
            email.attach(filename=photo_1.name, mimetype=photo_1.content_type, content=photo_1.read())

        photo_2 = request.FILES.get('photo_2', 0)
        if photo_2:
            email.attach(filename=photo_2.name, mimetype=photo_2.content_type, content=photo_2.read())

        photo_3 = request.FILES.get('photo_3', 0)
        if photo_3:
            email.attach(filename=photo_3.name, mimetype=photo_3.content_type, content=photo_3.read())

        photo_4 = request.FILES.get('photo_4', 0)
        if photo_4:
            email.attach(filename=photo_4.name, mimetype=photo_4.content_type, content=photo_4.read())

        photo_5 = request.FILES.get('photo_5', 0)
        if photo_5:
            email.attach(filename=photo_5.name, mimetype=photo_5.content_type, content=photo_5.read())

        photo_6 = request.FILES.get('photo_6', 0)
        if photo_6:
            email.attach(filename=photo_6.name, mimetype=photo_6.content_type, content=photo_6.read())    

        email.send()

        messages.success(request, 'Dziękujemy! Zgłosiłeś do nas swoją nieruchomość, wkrótce się z Tobą skontaktujemy')
        return render(request, 'publish/publish.html')
