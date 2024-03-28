from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from product.models import Product

@api_view(['POST'])
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ReviewSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(product=product, user=request.user)  # Assuming user is authenticated
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)

@api_view(['GET'])
def get_product_reviews(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.products_review.all()  # Fetch all reviews related to the product
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

