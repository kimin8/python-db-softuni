# Generated by Django 5.0.4 on 2024-07-04 23:08

from django.db import migrations
from django.utils import timezone


def modify_based_on_status(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')
    for order in order_model.objects.all():
        if order.status == 'Pending':
            order.delivery = order.order_date + timezone.timedelta(days=3)
            order.save()
        elif order.status == 'Completed':
            order.warranty = '24 months'
            order.save()
        elif order.status == 'Cancelled':
            order.delete()


def reverse_modify_based_on_status(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')
    for order in order_model.objects.all():
        if order.status == 'Pending':
            order.delivery = None
        elif order.status == 'Completed':
            order.warranty = order._meta.get_field('warranty').default
        order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_order'),
    ]

    operations = [
        migrations.RunPython(modify_based_on_status, reverse_code=reverse_modify_based_on_status)
    ]
