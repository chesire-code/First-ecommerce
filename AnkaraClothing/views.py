from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import (smartphone,earphones,bt_speaker,cover,USB_drive,charger,
                     OrderOffer,OrderTrending,OfferOrder,TrendingOrder,Subscribers, offer, bestseller
)
from django.views.generic.detail import DetailView
from .forms import SearchForm, SubscribeForm
from django.db.models import Q

def products(request):

    context = {
        'smartphones': smartphone.objects.all(),
        'offers' : offer.objects.all(),
        'bestsellers' : bestseller.objects.all(),
    }

    return render(request, 'AnkaraClothing/home.html', context)

class OfferDetailView(DetailView):
    model = offer
    template_name = 'AnkaraClothing/offer_detail.html'

class SmartphoneDetailView(DetailView):
    model = smartphone
    template_name = 'AnkaraClothing/smartphone_detail.html'

class CoverDetailView(DetailView):
    model = cover
    template_name = 'AnkaraClothing/cover_detail.html'

class EarphonesDetailView(DetailView):
    model = earphones
    template_name = 'AnkaraClothing/earphones_detail.html'

class ChargerDetailView(DetailView):
    model = charger
    template_name = 'AnkaraClothing/charger_detail.html'

class Bt_speakerDetailView(DetailView):
    model = bt_speaker
    template_name = 'AnkaraClothing/bt_speaker_detail.html'

class BestsellerDetailView(DetailView):
    model = bestseller
    template_name = 'AnkaraClothing/bestseller_detail.html'

@login_required
def trending_add_to_cart(request, slug):
    item = get_object_or_404(charger, slug=slug)
    order_item, created = OrderTrending.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = TrendingOrder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("product", slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = TrendingOrder.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("product", slug=slug)

@login_required
def trending_remove_from_cart(request, slug):
    item = get_object_or_404(charger, slug=slug)
    order_qs = TrendingOrder.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order_qs[0].items.filter(item__slug=item.slug).exists():
            order_item = OrderTrending.objects.filter(
                    item=item,
                    user=request.user,
                    ordered=False
                )[0]
            order_qs[0].items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("offer", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)

def cart(request):
    my_trending_cart = OrderTrending.objects.filter(user=request.user)



    for the_trending in my_trending_cart:
        trending_price_each = the_trending.item.price
        trending_total_price = trending_price_each * the_trending.quantity


    context = {
        'offer_carts' : OrderOffer.objects.filter(user=request.user),
        'trending_carts' : OrderTrending.objects.filter(user=request.user),

    }

    return render(request, 'AnkaraClothing/cart.html', context)

def subscribe(request):
    form = SubscribeForm(request.GET)
    if form.is_valid():
        mail = form.cleaned_data['mail']
        subscriber = Subscribers(mail=mail)
        subscriber.save()

    else:
        print("not saved")

    contexts = {
        'form' : form
    }

    return render(request, 'AnkaraClothing/home.html', contexts)

def search(request):
    global offer_results
    form = SearchForm(request.GET)
    trending_results = []
    if form.is_valid():
        query = request.GET.get('query', '')
        maxprice = request.GET.get('maxprice', 0)

        try:
            the_maxprice = int(float(maxprice))

        except:
            the_maxprice = 0

        if the_maxprice == 0 or '':
            smartphone_results = smartphone.objects.filter(descriptions__icontains=query)
            charger_results = charger.objects.filter(descriptions__icontains=query)
            cover_results = cover.objects.filter(descriptions__icontains=query)
            USB_drive_results = USB_drive.objects.filter(descriptions__icontains=query)
            bt_speaker_results = charger.objects.filter(descriptions__icontains=query)
            offer_results = offer.objects.filter(descriptions__icontains=query)

        if the_maxprice > 0:
            smartphone_results = charger.objects.filter(descriptions__icontains=query, price__lte=the_maxprice)
            charger_results = charger.objects.filter(descriptions__icontains=query, price__lte=the_maxprice)
            cover_results = charger.objects.filter(descriptions__icontains=query, price__lte=the_maxprice)
            USB_drive_results = charger.objects.filter(descriptions__icontains=query, price__lte=the_maxprice)
            bt_speaker_results = charger.objects.filter(descriptions__icontains=query, price__lte=the_maxprice)
            offer_results = offer.objects.filter(descriptions__icontains=query, price__lte=the_maxprice)

    trending_results += [smartphone_results, charger_results, cover_results, USB_drive_results, bt_speaker_results]

    contexts = {

        'smartphones' : smartphone_results,
        'chargers' : charger_results,
        'form' : form,
        'offers' : offer_results,
        'number_offers' : offer_results.count(),
        'number_others' : smartphone_results.count() + charger_results.count(),
        'query' : query,

    }

    return render(request, 'AnkaraClothing/search.html', contexts)

def search_smartphone(request):
    category = "smartphones"
    return render(request, 'AnkaraClothing/category.html', {'products' : smartphone.objects.all(),
                                                            'category' : category,
                                                            'offers' : offer.objects.filter(descriptions__icontains = "smartphone")})

def search_chargers(request):
    return render(request, 'AnkaraClothing/search.html', {'the_chargers' : smartphone.objects.all()})

def search_covers(request):
    return render(request, 'AnkaraClothing/search.html', {'the_covers' : smartphone.objects.all()})

def search_bt_speakers(request):
    return render(request, 'AnkaraClothing/search.html', {'the_bt_speakers' : smartphone.objects.all()})

def search_protectors(request):
    return render(request, 'AnkaraClothing/search.html', {'the_protectors' : smartphone.objects.all()})

def page_not_found(request, exception):
    return render(request, 'AnkaraClothing/404.html')
