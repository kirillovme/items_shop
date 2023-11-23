import stripe
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.urls import reverse

from order.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_stripe_session(request: HttpRequest, order_id: int) -> JsonResponse:
    """Возвращает id stripe сессии."""
    order = Order.objects.get(pk=order_id)
    discount_factor = 1
    if order.discount:
        discount_factor -= order.discount.discount_percent / 100
    tax_factor = 1
    if order.tax:
        tax_factor += order.tax.tax_percent / 100
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * discount_factor * tax_factor * 100),
            },
            'quantity': 1,
        } for item in order.items.all()],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('order_success')),
        cancel_url=request.build_absolute_uri(reverse('order_cancel')),
    )
    return JsonResponse({'id': session.id})


def order_detail(request: HttpRequest, order_id: int) -> HttpResponse:
    """Возвращает страницу с информацией о заказе с учетом налога и скидки."""
    order = get_object_or_404(Order, pk=order_id)
    discount_factor = 1
    if order.discount:
        discount_factor = 1 - (order.discount.discount_percent / 100)
    tax_factor = 1
    if order.tax:
        tax_factor = 1 + (order.tax.tax_percent / 100)
    items_with_final_price = []
    total_price = 0
    for item in order.items.all():
        final_item_price = item.price * discount_factor * tax_factor
        total_price += final_item_price
        items_with_final_price.append({
            'name': item.name,
            'original_price': item.price,
            'final_price': final_item_price
        })
    context = {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'order': order,
        'items_with_final_price': items_with_final_price,
        'total_price': total_price
    }
    return render(request, 'order/order_detail.html', context)


def payment_success(request: HttpRequest) -> HttpResponse:
    """Возвращает страницу при успешной оплате заказа."""
    return HttpResponse("Order checkout succeeded!")


def payment_cancel(request: HttpRequest) -> HttpResponse:
    """Возвращает страницу при отмененной оплате заказа."""
    return HttpResponse("Order checkout was cancelled.")
