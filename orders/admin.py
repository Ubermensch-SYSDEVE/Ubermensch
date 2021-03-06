from django.contrib import admin

# Register your models here.
from orders.models import Order, OrderLine, InspectorReport, Contract, BillingStatement, OfficialReceipt, \
    DeliveryReceipt, ProgressReport, AcceptanceLetter, PullOutSlip

admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(InspectorReport)
admin.site.register(Contract)
admin.site.register(BillingStatement)
admin.site.register(OfficialReceipt)
admin.site.register(DeliveryReceipt)
admin.site.register(ProgressReport)
admin.site.register(AcceptanceLetter)
admin.site.register(PullOutSlip)