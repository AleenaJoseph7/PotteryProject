from django.contrib import admin
from Myapp.models import catergorydb,productdb,potterydb
from webapp.models import Orderdb,Bookingdb,Cartdb,Checkoutdb
# Register your models here.
admin.site.register(catergorydb)
admin.site.register(productdb)
admin.site.register(potterydb)
admin.site.register(Orderdb)
admin.site.register(Bookingdb)
admin.site.register(Cartdb)
admin.site.register(Checkoutdb)