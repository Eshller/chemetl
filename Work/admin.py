from django.contrib import admin
from .models import Product , Material , Contact
# Register your models here.
admin.site.site_header = "ChemE Tl Management"
admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Contact)
