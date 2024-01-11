from django.shortcuts import render
from .models import Item
def item_list(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request,'homepage.html', context)

def product_page(request):
    return render(request, 'product-page.html')

def checkout(request):
    return render(request, 'checkout-page.html')