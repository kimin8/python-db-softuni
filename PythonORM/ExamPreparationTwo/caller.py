import os
from decimal import Decimal

import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order


def get_profiles(search_string=None):
    if search_string is None:
        return ""

    profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone_number__icontains=search_string)
    ).order_by('full_name')

    if profiles:
        result = []
        for profile in profiles:
            profile_orders = profile.order_set.count()
            result.append(f"Profile: {profile.full_name}, email: {profile.email}, phone number: {profile.phone_number}, orders: {profile_orders}")
        return "\n".join(result)
    else:
        return ""


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()
    if loyal_profiles:
        result = []
        for profile in loyal_profiles:
            profile_orders = profile.order_set.count()
            result.append(f"Profile: {profile.full_name}, orders: {profile_orders}")
        return "\n".join(result)
    else:
        return ""


def get_last_sold_products():
    latest_order = Order.objects.order_by('-creation_date').first()

    if not latest_order:
        return ""

    products_from_order = latest_order.products.all().order_by('name')

    names = [prod.name for prod in products_from_order]
    return f"Last sold products: {', '.join(names)}" if names else ""


def get_top_products():
    if not Order.objects.all().exists():
        return ""

    top_products = Product.objects.annotate(
        orders_count=Count('order')
    ).filter(
        orders_count__gt=0
    ).order_by(
        '-orders_count',
        'name'
    )[:5]

    if not top_products.exists():
        return ""

    product_lines = "\n".join(f"{p.name}, sold {p.orders_count} times" for p in top_products)
    return f"Top products:\n" + product_lines


def apply_discounts():
    filtered_orders = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2,
        is_completed=False
    )

    if filtered_orders.exists():
        affected = filtered_orders.count()

        filtered_orders.update(
            total_price=F('total_price') * 0.90
        )

        return f"Discount applied to {affected} orders."
    else:
        return f"Discount applied to 0 orders."


def complete_order():
    oldest_order = Order.objects.filter(
        is_completed=False,
    ).order_by(
        'creation_date'
    ).first()

    if not oldest_order:
        return ""

    for product in oldest_order.products.all():
        product.in_stock -= 1
        if product.in_stock == 0:
            product.is_available = False
        product.save()

    oldest_order.is_completed = True
    oldest_order.save()

    return "Order has been completed!"
