from django.shortcuts import render,redirect,get_object_or_404
from .models import *  
from .forms import *
from django.contrib.auth import logout
from r_final import settings
from django.core.mail import send_mail
import random
from .models import regisdata, cart  
from adminapp.models import add_book_cls, order

# Create your views here.
def home(request):
    product = add_book_cls.objects.all()
    return render(request, 'home.html',{'product':product})

def shop(request): 
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    product = add_book_cls.objects.all() 
    return render(request, 'book_list.html', {'product': product})

def book_detail(request, id):
    return render(request, 'book_detail.html')

def view_cart(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    cart_items = cart.objects.filter(user_id=user_id)
    
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    cart_items = cart.objects.filter(user_id=user_id)
    if not cart_items:
        return redirect('shop')
    
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        form = checkout_form(request.POST)
        if form.is_valid():
            order_obj = form.save(commit=False)        
            user_obj = regisdata.objects.get(id=user_id)
            order_obj.user = user_obj
            order_obj.total_price = total_price
            
            order_obj.save() 
            
            cart_items.delete()
            return render(request, 'order_success.html')
        else:
            
            print("Form Errors:", form.errors) 
    else:
        form = checkout_form()

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price, 'form': form})

def order_success(request):
    return render(request, 'order_success.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = regisdata.objects.filter(username=username,password=password).first()

        if user:
            request.session["user_id"] = user.id
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form=register_form(request.POST)
        if form.is_valid():
            form.save() 
            global otp
            otp=random.randint(11111,99999)
            sub="Your OTP for Verification"
            mail_msg=f"Dear User\n\nThanks for registration with us!\nYour Email Verification code is {otp}.\nPlease verify your account and enjoy our services!\n\nThank & Regards\nNotesApp Team\n+91 9429190565 | rutvimandaliya19@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]

            send_mail(subject=sub,message=mail_msg,from_email=from_ID,recipient_list=to_ID) 
            return redirect('otpverify')
        else:  
            print(form.errors)  
    return render(request, 'register.html')

def otpverify(request):
    global otp
    msg=""
    if request.method=='POST':
        if otp==int(request.POST["otp"]): 
            print("Verification Successfull")
            
            return redirect("login")
        else:
            msg="Sorry!Verfication faild....Try again!"
    return render(request,'otpverify.html',{'msg':msg})
   

def profile_view(request):
    orders = checkout.objects.all().order_by('-id')     
    return render(request, 'profile.html',{'orders':orders})

def contact(request):
    uid = request.session.get("user_id")

    if not uid:
        return redirect('login')

    form = contact_form()

    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')

    return render(request, 'contact.html', {'form': form})


def logout_view(request):
    return render(request, 'home.html')

def edit_profile(request):
    uid = request.session.get("user_id")

    if not uid:
        return redirect('login')

    try:
        user = regisdata.objects.get(id=uid)
    except regisdata.DoesNotExist:
        return redirect('login')

    if request.method == 'POST':
        
        updateReq = register_form(request.POST, instance=user)
        if updateReq.is_valid():
            updateReq.save()
            print("Profile Updated!")
            return redirect("profile") 
    else:
        updateReq = register_form(instance=user)
    return render(request, 'edit_profile.html', {'user': user, 'form': updateReq})

def user_logout(request):
    logout(request)
    return redirect('login')

def add_to_cart(request, id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    product = get_object_or_404(add_book_cls, id=id)

    cart_item, created = cart.objects.get_or_create(
        user_id=user_id,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def book_detail(request, id):
    book = get_object_or_404(add_book_cls, id=id)
    return render(request, 'book_detail.html', {'book': book})

def notes(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    if request.method=='POST':
        form = notes_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("notes upload successfully!!")
        else:
            print("error to save note!")    
    return render(request,'notes.html')
