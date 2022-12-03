# Generated by Django 4.1 on 2022-10-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_paid_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
