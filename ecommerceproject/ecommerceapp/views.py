from django.shortcuts import render


def index(request):
	return render(request,'ecommerceapp/index.html')

def about(request):
	return render(request,'ecommerceapp/about.html')

def bloggrid(request):
	return render(request,'ecommerceapp/blog-grid-left-sidebar.html')

def blogsingle(request):
	return render(request,'ecommerceapp/blog-single-left-sidebar.html')

def cart(request):
	return render(request,'ecommerceapp/cart.html')

def checkout(request):
	return render(request,'ecommerceapp/checkout.html')

def compare(request):
	return render(request,'ecommerceapp/compare.html')

def contact(request):
	return render(request,'ecommerceapp/contact.html')

def index11(request):
	return render(request,'ecommerceapp/index-11.html')

def index15(request):
	return render(request,'ecommerceapp/index-15.html')

def index17(request):
	return render(request,'ecommerceapp/index-17.html')

def index6(request):
	return render(request,'ecommerceapp/index-6.html')

def login(request):
	return render(request,'ecommerceapp/login.html')

def myaccount(request):
	return render(request,'ecommerceapp/my-account.html')

def shopleft(request):
	return render(request,'ecommerceapp/shop-left-sidebar.html')

def singleproduct(request):
	return render(request,'ecommerceapp/single-product-tabstyle-2.html')

def wishlist(request):
	return render(request,'ecommerceapp/wishlist.html')
