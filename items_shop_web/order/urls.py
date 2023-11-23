from django.urls import path
from order import views

urlpatterns = [
    path('checkout/<int:order_id>/', views.get_stripe_session, name='get_stripe_session'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/success/', views.payment_success, name='order_success'),
    path('order/cancel/', views.payment_cancel, name='order_cancel'),
]