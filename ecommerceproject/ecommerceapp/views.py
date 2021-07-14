from django.shortcuts import render, redirect
from .forms import ContactForm
from .forms import CreateUserForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login as logi
from django.contrib.auth import get_user_model 
from django.contrib import messages





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
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subj = "Website Inquiry" 
			# we can change the body of our message as required 
			body = {
			'name': form.cleaned_data['name'],  
			'email': form.cleaned_data['email'], 
			'subject': form.cleaned_data['subject'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())
			try:
				send_mail(subj, message, 'technocolabstest123@gmail.com', ['technocolabstest123@gmail.com'])	
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render(request,'ecommerceapp/contact.html') 
	form = ContactForm()
	return render(request, "ecommerceapp/contact.html", {'form':form})


def index11(request):
	return render(request,'ecommerceapp/index-11.html')

def index15(request):
	return render(request,'ecommerceapp/index-15.html')

def index17(request):
	return render(request,'ecommerceapp/index-17.html')

def index6(request):
	return render(request,'ecommerceapp/index-6.html')

def login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is None:
			User = get_user_model()
			user_queryset = User.objects.all().filter(email__iexact=username)
			if user_queryset:
				username = user_queryset[0].username
				user = authenticate(username=username, password=password)
		if user is not None:
			logi(request,user)
			return redirect('index')
		else:
			messages.info(request,'username or password is incorrect')
	
	context={}
	return render(request,'ecommerceapp/login.html',context)

def Register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			user.email=username			
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form':form}
	return render(request, 'ecommerceapp/login.html', context)


def myaccount(request):
	return render(request,'ecommerceapp/my-account.html')

def shopleft(request):
	return render(request,'ecommerceapp/shop-left-sidebar.html')

def singleproduct(request):
	return render(request,'ecommerceapp/single-product-tabstyle-2.html')

def wishlist(request):
	return render(request,'ecommerceapp/wishlist.html')

