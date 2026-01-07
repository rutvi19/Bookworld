from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('cart/', views.view_cart, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
    # path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    
    # Auth URLs
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('cart/', views.cart, name='cart'), 
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('notes/',views.notes,name='notes'),
] 