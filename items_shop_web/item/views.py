import stripe
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse

from item.models import Item
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_stripe_session(request: HttpRequest, item_id: int) -> JsonResponse:
    """Возвращает id stripe сессии."""
    item = Item.objects.get(pk=item_id)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('payment_success')),
        cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
    )
    return JsonResponse({'id': session.id})


def item_detail(request: HttpRequest, item_id: int) -> HttpResponse:
    """Возвращает страницу с описанием товара и кнопкой покупки."""
    item = Item.objects.get(pk=item_id)
    context = {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'item': item
    }
    return render(request, 'item/item_detail.html', context)


def payment_success(request: HttpRequest) -> HttpResponse:
    """Возвращает страницу при успешной оплате предмета."""
    return HttpResponse("Item payment succeeded!")


def payment_cancel(request: HttpRequest) -> HttpResponse:
    """Возвращает страницу при отмененной оплате предмета."""
    return HttpResponse("Item payment was cancelled.")
