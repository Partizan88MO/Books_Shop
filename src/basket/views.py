from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from . import models, forms
from basket import models as good_model
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView
from django.views import generic 
User = get_user_model()

 # Create your views here.

def order_detail(request, pk):
    obj = models.Order.objects.get(pk=pk)
    context = {"obj": obj, "verb": "Detail"}
    return render(
        request,
        template_name="basket/order_detail.html",
        context=context
        )

def order_list(request):
    form =forms.OrderForm()
    obj_list = models.Order.objects.all()
    context = {"object_list": obj_list, "verb": "List", "form": form}
    return render(
        request,
        template_name="basket/order_list.html",
        context=context
        )

def order_create(request):
    template_name = "basket/order_create.html"
    if request.method == "GET": 
        form =forms.OrderForm()
        context = {"verb": "Create", "form": form}
    elif  request.method == "POST":
        form =forms.OrderForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(f"/basket/order/{obj.pk}")
        else:
            context = {"verb": "Create", "form": form}
    else:
        raise Exception("Wrong method") 
    return render(
        request,
        template_name=template_name,
        context=context
        ) 

def order_update(request, pk):
    if request.method == "GET":
        template_name = "basket/order_update.html"
        obj = models.Order.objects.get(pk=pk)
        form = forms.OrderForm()
        context = {
            "obj":obj ,
            "verb": "Update",
            "form": form
            }
    elif  request.method == "POST":
        form =forms.OrderForm(request.POST)
        if form.is_valid():
            form.update_obj(pk)
        return HttpResponseRedirect(f"/basket/order/{pk}")
    else:
        raise Exception("Wrong method") 
    return render(
        request,
        template_name=template_name,
        context=context
        )

class AboutUs(TemplateView):
    template_name = "about_us.html"

class OrderList(generic.ListView):
    template_name = "basket/order_list.html"
    model = models.Order  

class OrderDetail(DetailView):
    template_name = "basket/order_detail.html"
    model = models.Order
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "Detail"
        return context # {}
    
class OrderUpdate(UpdateView):
    template_name = "basket/order_update.html"
    model = models.Order
    form_class = forms.OrderForm

    def get_success_url(self):
        return f"/basket/order/{self.object.pk}/"

class OrderCreate(CreateView):
    template_name = "basket/order_create.html"
    model = models.Order
    form_class = forms.OrderForm    
    
    def get_success_url(self):
        return f"/basket/order/{self.object.pk}/"
    
class OrderDelete(generic.DeleteView):
    template_name = "basket/order_delete.html"
    model = models.Order    
    success_url = "/basket/order/"

def update_cart(request):
    cart = None
    cart_id = request.session.get("cart_id")
    quantity = request.GET.get("quantity")
    good_pk = request.GET.get("good")  
    if quantity and good_pk:         
        user = request.user
    if request.user.is_anonymous:
        user = None 
    cart, created = models.Cart.objects.get_or_create(
        pk=cart_id,
        defaults={
            "customer": user
        }
    )
    if created:
        request.session["cart_id"] = cart.pk
    good = good_model.Book.objects.get(pk=int(good_pk))
    good_in_cart, created = models.GoodInCart.objects.get_or_create(
        cart=cart,
        good=good,
        defaults= {
            "quantity": int(quantity)
        }
    )
    if not created:
            good_in_cart.quantity = good_in_cart.quantity + int(quantity)
            good_in_cart.save()
    else:
        cart = models.Cart.objects.filter(pk=cart_id)
        if cart:
            cart = cart[0]
    return cart        

def cart(request):
    cart = update_cart(request)
    return render(
        request=request,
        template_name="basket/cart.html",
        context={"cart": cart}
    )
