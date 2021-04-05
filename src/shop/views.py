from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator



def product_list(request, category_slug=None):
 	category = None
 	categories = Category.objects.all()
	#product_list = Product.objects.all()
 	products = Product.objects.filter(available=True)
	
 	if category_slug:
 		category = get_object_or_404(Category, slug=category_slug)
 		products = products.filter(category=category)

	#paginator = Paginator(product_list, 3)
	#page_number = request.GET.get('page')
	#product_list = paginator.get_page(page_number)
 	return render(request,'product/list.html',{'category': category,
												'categories': categories,
												'products': products })


def product_detail(request, id, slug):
 	product = get_object_or_404(Product,id=id,slug=slug,available=True)
 	
 	return render(request,'product/detail.html',{'product': product})

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id,slug=slug,available=True)
	cart_product_form = CartAddProductForm()
	return render(request,'product/detail.html',{'product': product,'cart_product_form': cart_product_form})