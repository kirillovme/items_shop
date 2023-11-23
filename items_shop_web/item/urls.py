from django.urls import path
from item import views

urlpatterns = [
    path('buy/<int:item_id>/', views.get_stripe_session, name='get_stripe_session'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
]
