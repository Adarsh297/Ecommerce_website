from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created= order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartitems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0 ,'get_cart_items':0}
    products=product.objects.all()
    return render(request,'store.html',{'products':products , 'cartitems': cartitems})
    

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        Order,created= order.objects.get_or_create(customer=customer,complete=False)
        items=Order.Orderitem_set.all()
        cartitems=Order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0 ,'get_cart_items':0}
        cartitems= Order.get_cart_items
    
    products=product.objects.all()
    return render(request,'cart.html',{'products':products , 'cartitems': cartitems})

def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        Order,created= order.objects.get_or_create(customer=customer,complete=False)
        items=Order.Orderitem_set.all()
        cartitems=Order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0 ,'get_cart_items':0}
        cartitems= Order.get_cart_items
    products=product.objects.all()
    return render(request,'checkout.html',{'products':products , 'cartitems': cartitems})

def updateitem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('action:' ,action)
    print('productId:' ,productId)

    customer = request.user.customer
    product = product.objects.get(id=productId)
    Order,created= order.objects.get_or_create(customer=customer,complete=False)

    OrderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
       OrderItem.quantity = (OrderItem.quantity + 1)
    elif action == 'remove':
      OrderItem.quantity = (OrderItem.quantity - 1)

    OrderItem.save()

    if OrderItem.quantity <= 0:
      OrderItem.delete()

    return JsonResponse('item added',safe=False)