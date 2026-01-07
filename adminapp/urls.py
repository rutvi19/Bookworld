from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_books/', views.admin_books, name='admin_books'),
    path('admin_add_book/', views.admin_add_book, name='admin_add_book'),
    path('admin_orders/', views.admin_orders, name='admin_orders'),
    path('admin_users/', views.admin_users, name='admin_users'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_edit_pro/<int:id>/', views.admin_edit_pro, name='admin_edit_pro'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('order_delete/<int:id>/',views.order_delete,name='order_delete'),
    path('user_delete/<int:id>/',views.user_delete,name='user_delete'),
    path('admin_contact/', views.admin_contact, name='admin_contact'),
    path('admin_notes/',views.admin_notes,name='admin_notes'),


]