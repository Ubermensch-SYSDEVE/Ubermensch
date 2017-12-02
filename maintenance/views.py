import random
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Ubermensch import helper
from core.models import Profile
from maintenance.forms import MaintenanceContractForm
from maintenance.models import MaintenanceContract
from orders.models import Order, BillingStatement


@login_required
def maintenance_overview(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        context = {
            'order': order
        }

        return render(request, 'maintenance/maintenance.html', context)

    except Order.DoesNotExist:
        raise Http404('Order Does Not Exist')


@login_required
def maintenance_contract_view(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        expiration_date = order.contract.warranty_expiration_date
        contracts = MaintenanceContract.objects.all()
        maintenance_expiration_date = ''

        if MaintenanceContract.objects.all().count() == 0:
            current_contract = None
        else:
            current_contract = MaintenanceContract.objects.filter(is_current=True)[0]

        if current_contract is not None:
            maintenance_expiration_date = helper.add_years(
                current_contract.date_generated,
                current_contract.duration
            )

        context = {
            'order': order,
            'expiration_date': expiration_date,
            'is_warranty_period': expiration_date > datetime.now().date(),
            'contracts': contracts,
            'current_contract': current_contract,
            'maintenance_expiration_date': maintenance_expiration_date,
            'date_intervals': helper.get_date_intervals(
                current_contract.date_generated,
                maintenance_expiration_date,
                # terms of payment
                current_contract.payment
            )
        }

        return render(request, 'maintenance/maintenance_contract_overview.html', context)

    except Order.DoesNotExist:
        raise Http404('Order Does Not Exist')


@login_required
def add_maintenance_contract(request, order_id):
    try:
        order = Order.objects.get(id=order_id)

        form = MaintenanceContractForm(request.POST or None)

        context = {
            'form': form
        }

        if form.is_valid():
            contract = form.save(commit=False)
            contract.order = order

            number = random.randint(1, 999999)
            mc_no = "MC-" + str(number)

            while helper.check_duplicate_numbers(mc_no, 'maintenance'):
                number = random.randint(1, 999999)
                mc_no = "MC-" + str(number)

            profile = Profile.objects.get(user=request.user)
            contract.number = mc_no
            contract.generated_by = profile
            contract.is_current = True
            contract.save()

            messages.success(request, 'Maintenance contract added!')
            return redirect('maintenance:overview', order_id=order.id)

        return render(request, 'maintenance/maintenance_form.html', context)
    except Order.DoesNotExist:
        raise Http404('Order does not exist')


@login_required
def generate_billing_statement(request):
    maintenance_id = request.POST['id']
    order_id = request.POST['order']
    order = Order.objects.get(id=order_id)
    maintenance_contract = MaintenanceContract.objects.get(id=maintenance_id)
    profile = Profile.objects.get(user=request.user)
    maintenance_expiration_date = helper.add_years(
                maintenance_contract.date_generated,
                maintenance_contract.duration
            )

    number = random.randint(1, 999999)
    bs_no = "BS-" + str(number)

    while helper.check_duplicate_numbers(bs_no, 'billing'):
        number = random.randint(1, 999999)
        bs_no = "BS-" + str(number)

    percentage = len(helper.get_date_intervals(maintenance_contract.date_generated, maintenance_expiration_date,
                              maintenance_contract.payment))

    item = str(percentage) + '% DOWN PAYMENT FOR MAINTENANCE SERVICE'

    BillingStatement.objects.create(
        order=order,
        number=bs_no,
        item=item,
        percentage=percentage,
        generated_by=profile,
        price=maintenance_contract.price
    )

    messages.success(request, 'Billing Statement Generated')
    return redirect('maintenance:contract-view', order_id=order.id)



