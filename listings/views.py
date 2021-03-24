from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, rooms_choices, transaction_choices, category_choices


# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_data').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def lisitng(request, listing_id):
    listing=get_object_or_404(Listing, pk=listing_id)

    context={
        'listing':listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list=Listing.objects.order_by('-list_data')

    #category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__iexact = category)

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
        
   #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact = city)

     #Transaction
    if 'transaction' in request.GET:
        transaction = request.GET['transaction']
        if transaction:
            queryset_list=queryset_list.filter(transaction__iexact = transaction)
    
    
     # Rooms
    if 'rooms' in request.GET:
        rooms = request.GET['rooms']
        if rooms:
            queryset_list=queryset_list.filter(rooms__lte=rooms)
        
     # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)
                
    context={
        'category_choices':category_choices,
        'transaction_choices':transaction_choices,
        'rooms_choices':rooms_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'values':request.GET,
    }

    return render(request, 'listings/search.html', context)
