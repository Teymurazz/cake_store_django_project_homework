from django.shortcuts import render, HttpResponse
from .models import Cake

def home_page(request):
    min = request.GET.get("min_price")
    max = request.GET.get("max_price")

    cakes = Cake.objects.all()

    if min:
        cakes = cakes.filter(price__gte=min)
    if max:
        cakes = cakes.filter(price__lte=max)
    
    data = {
        "tortlar": cakes
    }
    return render(request, "cakes/home.html", data)


def cake_detail_views(request, pk):
    cake = Cake.objects.get(id=pk)
    data = {
        "tort": cake
    }
    return render(request, "cakes/cake_details.html", data)

def about_us(request):
    return render(request, "cakes/about_us.html")

def contact(request):
    return render(request, "cakes/contact_us.html")

def forum(request):
    return render(request, "cakes/forum.html")

def faq(request):
    return render(request, "cakes/faq.html")