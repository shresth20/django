from django.shortcuts import render
from .models import DrinkVariety
from django.shortcuts import render, get_object_or_404
from .forms import ordersForm

# Create your views here.
def all_drinks(request):
    drinks = DrinkVariety.objects.all()
    return render(request, 'cafeteria/index.html', {'drinks':drinks})

def menu(request):
    return render(request, 'cafeteria/menu.html')

def menu_detail(request, menu_id):
  menu = get_object_or_404(DrinkVariety, pk=menu_id)
  return render(request, 'cafeteria/menu_detail.html', {'menu': menu})

def orders(request):
    stock = ''
    if request.method == 'POST':
        form =  ordersForm(request.POST)
        if form.is_valid():
            drinks = form.cleaned_data['orders']
            stock = f'{drinks} is in stock, Order is placed, You get your Order soon !!'
            # stock = Stock.objects.filter(DrinkVariety=DrinkVariety)
    else:
        form = ordersForm()
    return render(request, 'cafeteria/orders.html', {'form': form, 'stock': stock}) 


def about(request):
    return render(request, 'cafeteria/about.html')

def contact(request):
    return render(request, 'cafeteria/contact.html')
    