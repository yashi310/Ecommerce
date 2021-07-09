from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date

# Create your models here.

class Customer(models.Model):
	user= models.ForeignKey(User, on_delete= models.CASCADE)
	first_name=models.CharField(max_length=200,null=True,blank=True)
	last_name=models.CharField(max_length=200,null=True,blank=True)
	email = models.EmailField(max_length=254, null=True)
	mobile=models.IntegerField(max_length=12,null=True,blank=True)

	def __str__(self):
		return self.first_name

class Products(models.Model):
	pid=models.AutoField(primary_key=True)
	name=models.CharField(max_length=400,null=False)
	image=models.URLField(max_length=500)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	description=models.TextField(null=True,blank=True,max_length=1000)

	def __str__(self):
		return self.name

class Wishlist(models.Model):
	wid=models.AutoField(primary_key=True)
	user= models.ForeignKey(User,on_delete=models.CASCADE)
	pid=models.ForeignKey(Products,on_delete=models.CASCADE)
	create_date=models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.wid

class Order(models.Model):
	oid=models.AutoField(primary_key=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	address=models.TextField(max_length=300,null=True,blank=True)
	city= models.CharField(max_length=250,null=True,blank=True)
	pincode= models.IntegerField(max_length=15,blank=True,null=True)
	payment_type= models.CharField(max_length=150,blank=True,null=True)
	total_price= models.DecimalField(max_digits=10,decimal_places=2)
	payment_status= models.CharField(max_length=250,null=True,blank=True)
	order_status= models.CharField(max_length=250,null=True,blank=True)
	added_on= models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.oid






