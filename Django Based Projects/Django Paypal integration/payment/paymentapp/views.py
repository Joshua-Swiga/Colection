from django.shortcuts import render
from .models import Product

# Modules used for the payment
from django.conf import settings
import uuid
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm


def store(request):
    products = Product.objects.all()

    return render (request, 'store.html',{
        "products": products,
    })


# For rendering individual content...
from django.urls import reverse

from django.urls import reverse

def individual(request, pk):
    item_id = Product.objects.get(id=pk)

    host = request.get_host()
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': item_id.product_price,
        'item_name': item_id.product_name,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        # Fix the syntax here
        'return_url': f"http://{host}{reverse('payment-success', kwargs={'pk': item_id.id})}?price={item_id.product_price}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'pk': item_id.id})}",
    }
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    return render(request, 'each_item.html', {
        'selected_item': item_id,
        'paypal': paypal_payment,
    })




# Remove sucess page and have the loby. Include condition that checks whether the price is none or has value
# If it does, perform arithmetic operations to add Tokens. 
# If not, just render the template
def success(request, pk):
    item_id = Product.objects.get(id=pk)

    price = request.GET.get('price')
    return render(request, 'payment-success.html', {
        "item_id": item_id,
        "price": price,
    })



# Pilipili1
def failed(request, pk):
    item_id = Product.objects.get(id = pk)
    return render (request, 'payment-failed.html', {
        "item_id": item_id,
    })