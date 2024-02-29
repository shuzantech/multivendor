# # multivendor_api/account/admin.py

# from django.contrib import admin
# from .models import Profile, Seller, Customer, Product, Order

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'bio', 'profile_picture')

# @admin.register(Seller)
# class SellerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'shop_name', 'description')

# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'address')

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'price', 'seller_name')

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('customer_name', 'total_price', 'order_date')
#     filter_horizontal = ('products',)  # Allows for a more user-friendly interface for selecting products in an order
