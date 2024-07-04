# Generated by Django 5.0.4 on 2024-07-04 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_category_modify'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('customer_name', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('CO', 'Completed'), ('CA', 'Cancelled')], max_length=30)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('warranty', models.CharField(default='No warranty')),
                ('delivery', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
