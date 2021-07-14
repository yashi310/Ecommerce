
from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView,PasswordResetView,PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
      path('',views.index,name='index'),
      path('about/',views.about,name='about'),
      path('bloggrid/',views.bloggrid,name='bloggrid'),
      path('blogsingle/',views.blogsingle,name='blogsingle'),
      path('cart/',views.cart,name='cart'),
      path('checkout/',views.checkout,name='checkout'),
      path('compare/',views.compare,name='compare'),
      path('contact/',views.contact,name='contact'),
      path('index11/',views.index11,name='index11'),
      path('index15/',views.index15,name='index15'),
      path('index17/',views.index17,name='index17'),
      path('index6/',views.index6,name='index6'),
      path('login/',views.login,name='login'),
      path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
      path('Register/',views.Register,name='Register'),
      path("password-reset/", PasswordResetView.as_view(template_name='ecommerceapp/password_reset.html'), name="password_reset"),
      path("password-reset/done/", PasswordResetDoneView.as_view(template_name='ecommerceapp/password_reset_done.html'), name="password_reset_done"),
      path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name='ecommerceapp/password_reset_confirm.html'), name="password_reset_confirm"),
      path("password-reset-complete/", PasswordResetCompleteView.as_view(template_name='ecommerceapp/password_reset_complete.html'), name="password_reset_complete"),
      path('myaccount/',views.myaccount,name='myaccount'),
      path('shopleft/',views.shopleft,name='shopleft'),
      path('singleproduct/',views.singleproduct,name='singleproduct'),
      path('wishlist/',views.wishlist,name='wishlist'),
    
]
