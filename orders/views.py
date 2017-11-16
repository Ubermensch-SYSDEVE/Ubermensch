import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render
import json
from orders.forms import OrderForm
from orders.models import Order, OrderLine, InspectorReport
from products.models import Product


@login_required
def index(request):

    orders = Order.objects.all()
    return render(request, 'orders/index.html', {'orders': orders})


@login_required
def add_order(request):

    form = OrderForm(request.POST or None)
    orders = Order.objects.all()

    if form.is_valid():
        order = form.save(commit=False)
        order.save()

        messages.success(request, "Pending order placed")
        return render(request, 'orders/index.html', {'orders': orders})

    return render(request, 'orders/add_order.html', {'form': form})


@login_required
def order_details(request, order_id):
    try:
        order = Order.objects.get(id=order_id)

        context = {
            'order': order
        }

        return render(request, 'orders/order_detail.html', context)

    except Order.DoesNotExist:
        raise Http404("Order does not exist")


@login_required
def project_requirements_phase(request, order_id):
    try:
        order = Order.objects.get(id=order_id)

        context = {
            'order': order
        }

        return render(request, 'orders/project_requirements.html', context)

    except Order.DoesNotExist:
        raise Http404("Order does not exist")


@login_required
def purchase_order_phase(request, order_id):
    try:
        order = Order.objects.get(id=order_id)

        context = {
            'order': order
        }

        return render(request, 'orders/purchase_order_phase.html', context)

    except Order.DoesNotExist:
        raise Http404("Order does not exist")


@login_required
def product_retrieval_phase(request, order_id):
    try:
        order = Order.objects.get(id=order_id)

        context = {
            'order': order
        }

        return render(request, 'orders/product_retrieval.html', context)

    except Order.DoesNotExist:
        raise Http404("Order does not exist")


@login_required
def delivery(request, order_id):
    try:
        order = Order.objects.get(id=order_id)

        context = {
            'order': order
        }

        return render(request, 'orders/delivery.html', context)

    except Order.DoesNotExist:
        raise Http404("Order does not exist")


@login_required
def installation(request, order_id):
    try:
        order = Order.objects.get(id=order_id)

        context = {
            'order': order
        }

        return render(request, 'orders/installation.html', context)

    except Order.DoesNotExist:
        raise Http404("Order does not exist")


@login_required
def maintenance(request, order_id):
    try:
        order = Order.objects.get(id=order_id)

        context = {
            'order': order
        }

        return render(request, 'orders/maintenance.html', context)

    except Order.DoesNotExist:
        raise Http404("Order does not exist")


@login_required
def inspector_report(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        products = Product.objects.all()

        context = {
            'order': order,
            'products': products
        }

        return render(request, 'orders/inspector_report.html', context)

    except Order.DoesNotExist:
        raise Http404("Order does not exist")


@login_required
def add_order_line(request):
    order = Order.objects.get(id=request.POST['order'])
    product = Product.objects.get(id=request.POST['product'])
    quantity = request.POST['quantity']
    duration = request.POST['duration']
    manpower = request.POST['manpower']

    OrderLine.objects.create(
        order=order,
        product=product,
        quantity=quantity
    )

    order.has_project_requirements = True
    order.save()

    number = random.randint(1, 999999)
    inspector_no = "I-" + str(number)

    InspectorReport.objects.create(
        order=order,
        inspector_report_no=inspector_no,
        duration=duration,
        manpower=manpower
    )

    return HttpResponse("added")


@login_required
def view_inspector_report(request, order_id):

    try:
        order = Order.objects.get(id=order_id)
        order_line = OrderLine.objects.filter(order=order_id)
        report_inspector = InspectorReport.objects.get(order=order)

        context = {
            'order': order,
            'order_line': order_line,
            'inspector_report': report_inspector
        }

        return render(request, 'orders/inspector_report_R.html', context)

    except Order.DoesNotExist:
        raise Http404("Order does not exist")





