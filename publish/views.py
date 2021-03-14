from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'publish/publish.html')

def published(request):
    if request.method=='POST':
        listing =request.POST['listing']
        address =request.POST['address']
        city =request.POST['city']
        price =request.POST['price']
        bathrooms =request.POST['bathrooms']
        garage =request.POST['garage']
        sqft =request.POST['sqft']
        lot_size =request.POST['lot_size']
        photo_1 =request.POST['photo_1']
        photo_2 =request.POST['photo_2']
        photo_3 =request.POST['photo_3']
        photo_4 =request.POST['photo_4']
        photo_5 =request.POST['photo_5']
        photo_6 =request.POST['photo_6']
        name = request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        message =request.POST['message']
        user_id =request.POST['user_id']


        # Send mail

        send_mail (
                'Publikacja nieruchomosci',
                name + ' zapytał o nieruchomość:' + listing + '. Treść wiadomości:'+ message + 
                'tel:' + phone + photo_1 + photo_2 + garage + sqft + bathrooms + price,
                'mdom.zapytanie@gmail.com',
                ['patryk.mauer@gmail.com'],
                fail_silently=False
        )

        messages.success(request, 'Twoje zapytanie zostało wysłane, wkrótce się z Tobą skontaktujemy')
        return render(request, 'publish/publish.html')
