from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    
    path('individual_item/<int:pk>/', views.individual, name='individual'), # Should display individual element. 

    path('payment-success/<int:pk>/', views.success, name='payment-success'),
    path('payment-failed/<int:pk>/', views.failed, name='payment-failed'),

]