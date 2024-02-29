# # multivendor_api/account/serializers.py

# from rest_framework import serializers
# from .models import Profile, Seller, Customer, Product, Order

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['id', 'user', 'bio', 'profile_picture']

# class SellerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Seller
#         fields = ['id', 'user', 'shop_name', 'description', 'product_name']

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['id', 'user', 'address', 'orders']

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'description', 'price', 'seller_name']

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['id', 'customer_name', 'products', 'total_price', 'order_date']
