from rest_framework import serializers
from .models import Order, orderItem,  Product





class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderItem
        fields = ("id", "product", "price", "quantity")
        
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ("id","first_name","items",
        "last_name",
        "email",
        "zipcode",
        "address",
        "place",
        "phone",
        "created_at",
        "paid_amount")
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items_data:
            orderItem.objects.create(order = order, **item)
        return super().create(validated_data)
    
class MyOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ("id","first_name","items",
        "last_name",
        "email",
        "zipcode",
        "address",
        "place",
        "phone",
        "created_at",
        "paid_amount")