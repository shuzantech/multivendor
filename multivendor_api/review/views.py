from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm  # You need to create a form for handling review input
from django.contrib.auth.decorators import login_required

@login_required
def create_review(request, product_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product_id = product_id
            review.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ReviewForm()

    return render(request, 'create_review.html', {'form': form})

def product_detail(request, product_id):
    product_reviews = Review.objects.filter(product_id=product_id)
    return render(request, 'product_detail.html', {'product_reviews': product_reviews})
