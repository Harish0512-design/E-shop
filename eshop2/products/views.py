from django.shortcuts import render
from products.models import Product, Profile, Cart, Sold, Deliver
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.db.models import Q

# Create your views here.
@method_decorator(login_required,name="dispatch")
class ProductListView(ListView):
    model = Product
    def get_queryset(self):
        si = self.request.GET.get('si')
        if si==None:
            si=" "
        products = Product.objects.filter(Q(p_name__icontains=si)|Q(p_price__icontains=si)|Q(p_des__icontains=si))
        for p1 in products:
            p1.ordered = False
            ob = Cart.objects.filter(product = p1,p_name = p1.p_name,p_price=p1.p_price)
            if ob:
                p1.ordered = True
        return products
        
            
@method_decorator(login_required, name="dispatch")
class ProductDetailView(DetailView):
    model = Product
    
class AboutView(TemplateView):
    template_name = "products/about.html"
    
class ContactView(TemplateView):
    template_name = "products/contact.html"
    
    
@method_decorator(login_required, name="dispatch")
class ProfileEditView(UpdateView):
    model = Profile
    fields = ['name','profile_pic','gender','phone','hno','street','landmark','city','pincode','dist','state']
    template_name="products/profile_form.html"
    
@method_decorator(login_required, name="dispatch")
class CartView(ListView):
    model = Cart
    template_name="products/cart_form.html"
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        amounts = Cart.objects.all()
        total_amount = 0
        for a in amounts:
            Cart.objects.filter(product=a.product,p_name=a.p_name,p_price=a.p_price,p_quantity=a.p_quantity,p_img=a.p_img).update(amount = a.p_price * a.p_quantity)
        total_amounts = Cart.objects.all()
        for ta in total_amounts:
            total_amount += ta.amount
        data['no_of_items'] = total_amounts.count()
        data['total_amount'] = total_amount
        return data

@method_decorator(login_required, name="dispatch")
class OrderedView(ListView):
    template_name ="products/sold_form.html"
    def get_queryset(self):
        ordereditems = Cart.objects.all()
        for items in ordereditems:
            Sold.objects.create(user=self.request.user,p_name=items.p_name,p_price=items.p_price,p_img=items.p_img,amount=items.amount,p_quantity=items.p_quantity,p_instock=items.p_instock)
            Product.objects.filter(p_name=items.p_name).update(p_instock = items.p_instock - items.p_quantity) 
            Cart.objects.filter(p_name=items.p_name,p_price=items.p_price,p_img=items.p_img,amount=items.amount,p_quantity=items.p_quantity,p_instock=items.p_instock).delete()
              
            
        return HttpResponseRedirect(redirect_to="products/sold_form.html")
    
def recentsView(req,pk):
    profile = Profile.objects.get(pk=pk)
    recents = Deliver.objects.filter(name=profile.user).order_by("-id")
    
    lst1 = []
    for r in recents:
        rp = r.products.all()
        for ob in rp:
            ls = []
            lst = []
            img = ob.p_img
            ls.append(img)
            name = ob.p_name
            ls.append(name)
            price = ob.p_price
            ls.append(price)
            quantity = ob.p_quantity
            ls.append(quantity)
            amount = ob.amount
            ls.append(amount)
            delivered_on = ob.sold_on
            ls.append(delivered_on)
            lst.append(ls)
            lst1.append(lst)
        break
    lst2 = lst1           
    return render(req,"products/recents.html",{'lst' : lst2})      
def deliverview(req):
    items_to_sold = Sold.objects.filter(user=req.user)
    d1 = Deliver(name=req.user,cust_name=req.user.profile.name,phone=req.user.profile.phone,hno=req.user.profile.hno,street=req.user.profile.street,landmark=req.user.profile.landmark,city=req.user.profile.city,pincode=req.user.profile.pincode,dist=req.user.profile.pincode,state=req.user.profile.state)
    d1.save()
    for ci in items_to_sold:
       d1.products.add(ci)
    d1.save()
        
    
    return render(req,"products/confirm.html")
         
def cart(req,pk):
    product = Product.objects.get(pk=pk)
    Cart.objects.create(product=product,p_name=product.p_name,p_price=product.p_price,p_img=product.p_img,p_instock=product.p_instock)
    
    return HttpResponseRedirect(redirect_to = "/products/product_list")

def cartdel(req,pk):
    product = Product.objects.get(pk=pk)
    Cart.objects.filter(product=product,p_name=product.p_name,p_price=product.p_price,p_img=product.p_img).delete()
    return HttpResponseRedirect(redirect_to ="/products/product_list")    

def additemquantity(req,pk):
    item = Cart.objects.get(pk=pk)
    Cart.objects.filter(pk=item.pk).update(p_quantity=item.p_quantity+1)
    return HttpResponseRedirect(redirect_to="/products/cart")

def removeitemquantity(req,pk):
    item = Cart.objects.get(pk=pk)
    Cart.objects.filter(pk=item.pk).update(p_quantity=item.p_quantity-1)
    return HttpResponseRedirect(redirect_to="/products/cart")