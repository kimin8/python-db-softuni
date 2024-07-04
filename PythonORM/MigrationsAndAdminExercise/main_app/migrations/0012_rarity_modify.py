# Generated by Django 5.0.4 on 2024-07-04 22:16

from django.db import migrations


def modify_rarity(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')
    for item in item_model.objects.all():
        if item.price <= 10:
            item.rarity = 'Rare'
        elif 11 <= item.price <= 20:
            item.rarity = 'Very Rare'
        elif 21 <= item.price <= 30:
            item.rarity = 'Extremely Rare'
        elif item.price >= 31:
            item.rarity = 'Mega Rare'
        item_model.save()


def reverse_modify_rarity(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')
    for item in item_model.objects.all():
        item.rarity = 'No rarity'
        item_model.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_item'),
    ]

    operations = [
        migrations.RunPython(modify_rarity, reverse_code=reverse_modify_rarity)
    ]
