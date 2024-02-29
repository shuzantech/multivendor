# # multivendor_api/account/views.py

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# # from .models import Profile, Seller, Customer, Product, Order
# # from .serializers import ProfileSerializer, SellerSerializer, CustomerSerializer, ProductSerializer, OrderSerializer

# class ProfileAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         profile = request.user.profile
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, *args, **kwargs):
#         profile = request.user.profile
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, *args, **kwargs):
#         profile = request.user.profile
#         serializer = ProfileSerializer(profile, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         profile = request.user.profile
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class SellerAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         seller = request.user.seller
#         serializer = SellerSerializer(seller)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = SellerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, *args, **kwargs):
#         seller = request.user.seller
#         serializer = SellerSerializer(seller, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, *args, **kwargs):
#         seller = request.user.seller
#         serializer = SellerSerializer(seller, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         seller = request.user.seller
#         seller.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class CustomerAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         customer = request.user.customer
#         serializer = CustomerSerializer(customer)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, *args, **kwargs):
#         customer = request.user.customer
#         serializer = CustomerSerializer(customer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, *args, **kwargs):
#         customer = request.user.customer
#         serializer = CustomerSerializer(customer, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         customer = request.user.customer
#         customer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(seller=request.user.seller)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Implement put, patch, delete methods for Product as needed


# class OrderAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         orders = Order.objects.filter(customer=request.user.customer)
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(customer=request.user.customer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Implement put, patch, delete methods for Order as needed
