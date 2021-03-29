from django.shortcuts import render
from django.template import RequestContext
from listings.models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def handler404(request, *args, **argv):
    listings = Listing.objects.order_by('-list_data').filter(is_published=True)

    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

# def handler404(request, *args, **argv):
#     response = render_to_response('404.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response

# def handler500(request, *args, **argv):
#     response = render(request,'500.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 500
#     return response