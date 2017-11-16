from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from inventory.models import Product, Supplier, Category, Order, OrderLine


@login_required
def index(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'inventory/index.html', context)


def order_details_inventory(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        orderline = OrderLine.objects.get(id=order_id)

        context = {
            'order': order,
            'orderlines': orderline,
        }

        return render(request, 'inventory/order_detail_inventory.html', context)

    except Order.DoesNotExist:
        raise Http404("Order does not exist")


def inventory_order(request):
    orders = Order.objects.all()
    return render(request, 'inventory/inventory_order.html', {'orders': orders})