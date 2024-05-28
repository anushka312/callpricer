from django.contrib import admin
from django.urls import path
from views import callPriceCalc, CallPriceView

urlpatterns = [
    path('calculate-call-price/', callPriceCalc, name='call_price_calculation'),
    path('call-price-view/', CallPriceView, name='call_price_view'),
]
