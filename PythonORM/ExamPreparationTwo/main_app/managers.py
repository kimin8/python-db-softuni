from django.db import models
from django.db.models import Count, QuerySet


class ProfileManager(models.Manager):
    def get_regular_customers(self) -> QuerySet:
        return self.annotate(number_of_orders=Count('order')).filter(number_of_orders__gt=2).order_by('-number_of_orders')
