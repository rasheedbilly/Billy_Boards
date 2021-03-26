from django.contrib import admin
from .models import Stock
from .models import Product
from .models import Cart
from .models import Address
from .models import User
from .models import Order

# Register your models here.
admin.site.register(Stock)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(User)
admin.site.register(Order)
