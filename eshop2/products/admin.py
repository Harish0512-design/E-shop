from django.contrib import admin
from products.models import Cart, Product, Sold, Deliver,Profile
from django.contrib.admin.options import ModelAdmin


#Register your models here.
class ProductAdmin(ModelAdmin):
    list_display = ['p_name','p_price','p_instock']
    search_fields = ['p_date','p_instock']
    
class DeliverAdmin(ModelAdmin):
    list_display = ['name','sold_on']
    list_filter = ['sold_on']
    search_fields=['sold_on']    

class SoldAdmin(ModelAdmin):
    list_display = ['p_name','p_price','sold_on']
    search_fields = ['p_date','p_instock']
    list_filter = ['sold_on']
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart)
admin.site.register(Profile)
admin.site.register(Sold,SoldAdmin)
admin.site.register(Deliver,DeliverAdmin)