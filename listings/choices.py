from .models import Listing
listings = Listing.objects.order_by('-list_data').filter(is_published=True)
cities = []
cities_full=[]
for listing in listings:
    if listing.city not in cities:
        cities.append(listing.city)
        cities_full.append((listing.voivodeship, listing.city))


cities_full = sorted(cities_full)
# print (cities_full)
cities =[]
for city in cities_full:
    cities.append(city[1])

place=[]
for city in cities_full:
    name=', '.join(city)
    place.append(name)

cities_choices=dict(zip(cities, place))
print(cities_choices)

rooms_choices={

    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
}

price_choices={
    '1000':'1,000zł',
    '2000':'2,000zł',
    '3000':'3,000zł',
    '4000':'4,000zł',
    '5000':'5,000zł',
    '7000':'7,000zł',
    '10000':'10,000zł',
    '50000':'50,000zł',
    '100000':'100,000zł',
    '200000':'200,000zł',
    '300000':'300,000zł',
    '400000':'400,000zł',
    '500000':'500,000zł',
    '600000':'600,000zł',
    '700000':'700,000zł',
    '800000':'800,000zł',
    '900000':'900,000zł',
    '1000000':'1mln+ zł',

}

category_choices={
    'mieszkanie':'Mieszkanie',
    'dom':'Dom',
    'działka':'Działka',
    'lokal':'Lokal',
}

transaction_choices={
    'wynajem':'Wynajem',
    'sprzedaż':'Sprzedaż',
}


