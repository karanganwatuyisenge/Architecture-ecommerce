from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','title','brand','category','status')
    list_editable=('status',)
admin.site.register(Product,ProductAdmin)

#Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','product','price')
admin.site.register(ProductAttribute,ProductAttributeAdmin)