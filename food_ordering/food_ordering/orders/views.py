from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import CartItem, FoodItem


# Create your views here.
def login_page(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=email,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Invalid credentials'})
    return render(request,'login.html')

def signup_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=email,password=password)
        return redirect('login')
    return render(request,'signup.html')

def logout_user(request):
    logout(request)
    return redirect('login')


# Page Views
def home_page(request):
    return render(request, 'home.html')


def menu_page(request):
    food_items = FoodItem.objects.all()
    return render(request, 'menu.html', {'food_items': food_items})


def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.food_item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, food_id):
    food_item = FoodItem.objects.get(id=food_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, food_item=food_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def remove_from_cart(request, cart_id):
    cart_item = CartItem.objects.get(id=cart_id)
    cart_item.delete()
    return redirect('cart')


def about_page(request):
    return render(request, 'about.html')