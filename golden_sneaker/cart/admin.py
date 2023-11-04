from django.contrib import admin
from .models import Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ProductResource(resources.ModelResource):
   class Meta:
      model = Product
class ProductAdmin(ImportExportModelAdmin):
   resource_class = ProductResource

admin.site.register(Product, ProductAdmin)