from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import *
from .forms import *
from django.contrib.auth import logout
from .models import * 
from userapp.models import regisdata,notes_cls

# Create your views here.

def admin_dashboard(request):
    user = regisdata.objects.all()
    book = add_book_cls.objects.all()
    ord = order.objects.all()
    ords = order.objects.all()
    total_order = len(ord)
    total_book = len(book)
    total_user = len(user)
    return render(request, 'admin_dashboard.html',{'total_user':total_user,'total_book':total_book,'total_order':total_order,'ords':ords})

def admin_books(request):
    books = add_book_cls.objects.all()
    return render(request, 'admin_books.html',{'books':books})

def admin_add_book(request):
    if request.method == 'POST':
        form = add_book_form(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            print("Book Added Successfully")
        else:
            print(form.errors)    
    return render(request, 'admin_add_book.html')

def admin_orders(request):
    orders = checkout.objects.all().order_by('-id')     
    return render(request, 'admin_orders.html',{'orders' : orders})

def admin_users(request):
    users = regisdata.objects.all()
    return render(request, 'admin_users.html',{'users' : users}) 

def admin_login(request):
    if request.method == 'POST':
        unm = request.POST['username']
        pwd = request.POST['password']
        if unm == 'admin' and pwd == '123':
            print("admin login succesfully!!!!")
            return redirect('admin_dashboard')
        else:
            print("login invalid!!!")
    return render(request,'admin_login.html')

def admin_edit_pro(request, id): 
    book = get_object_or_404(add_book_cls, id=id) 
    if request.method == 'POST':
        updateReq = add_book_form(request.POST, request.FILES, instance=book)
        if updateReq.is_valid():
            updateReq.save()
            print("Updated Book Successfully!")
            return redirect("admin_books")
        else:
            print(updateReq.errors)
    return render(request, 'admin_edit_pro.html', {'book': book})

def logout_view(request):
    return render(request,'admin_login.html')

def admin_logout(request):
    logout(request)
    return render(request,'admin_login.html')

def order_delete(request, id):
    order = checkout.objects.get(id=id)
    order.delete()
    return redirect('admin_orders')

def user_delete(request, id):
    book = get_object_or_404(add_book_cls, id=id) 
    book.delete() 
    return redirect('admin_books')

def admin_contact(request):
    contact = contact_cls.objects.all()
    return render(request,'admin_contact.html',{'contact':contact})

def admin_notes(request):
    notes=notes_cls.objects.all()
    return render(request,'admin_notes.html',{'notes':notes})