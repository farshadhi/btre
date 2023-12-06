from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import bedroom_choices, price_choices, state_choices

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    contex = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', contex)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)

    #keywords
    keywords = request.GET.get("keywords")
    if keywords:
        queryset_list = queryset_list.filter(description__icontains = keywords)
    
    #city
    city = request.GET.get("city")
    if city:
        queryset_list = queryset_list.filter(city__iexact = city)
    
    #state
    state = request.GET.get("state")
    if state:
        queryset_list = queryset_list.filter(state__iexact = state)
    
    #bedrooms
    bedrooms = request.GET.get("bedrooms")
    if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)

    #price
    price = request.GET.get("price")
    if price:
        queryset_list = queryset_list.filter(price__lte = price)

    context = {
        'listings': queryset_list,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)