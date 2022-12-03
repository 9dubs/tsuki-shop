from rest_framework import serializers

from .models import Order, OrderItems

from product.serializers import ProductSerializer

from drf_writable_nested import WritableNestedModelSerializer

class MyOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = OrderItems
        fields = (
            "price",
            "product",
            "quantity",
        )

class MyOrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
            "paid_amount"
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
        )

        def create(self, validated_data):
            items_data = validated_data.pop('items')
            order = Order.objects.create(**validated_data)

            for item_data in items_data:
                OrderItems.objects.create(order=order, **item_data)

            return order
