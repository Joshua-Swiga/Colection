
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paymentapp.urls')),
    #path('', include('paymentconfig.urls')),
    path('', include('paypal.standard.ipn.urls')),
]
