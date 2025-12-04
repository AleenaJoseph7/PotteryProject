from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login
from Myapp.models import catergorydb,productdb,potterydb
from webapp.models import Orderdb,Bookingdb
import  datetime

from django.contrib import messages


# Create your views here.
def indexpage(request):
    category_count=catergorydb.objects.count()
    product_count=productdb.objects.count()
    order_count=Orderdb.objects.count()
    booking_count=Bookingdb.objects.count()
    pottery_count=potterydb.objects.count()

    date=datetime.datetime.now()
    return render(request,"index.html",{'date':date,'category_count':category_count,'product_count':product_count,
                                        'order_count':order_count,
                                        'booking_count':booking_count,
                                        'pottery_count':pottery_count})


def catergory(request):
    date = datetime.datetime.now()
    return render(request,"addcategory.html",{'date':date})

def savecatergory(request):
    if request.method=='POST':
        duration=request.POST.get('duration')
        ob=catergorydb(Duration=duration)
        ob.save()
        messages.success(request,"Catergory Saved Succesfully!")
        return redirect(catergory)

def displaycatergory(request):
    date = datetime.datetime.now()
    data=catergorydb.objects.all()
    return render(request,"displaycategory.html",{'data':data,'date':date})

def editcatergory(request,c_id):
    date = datetime.datetime.now()
    d=catergorydb.objects.get(id=c_id)
    return render(request,"editcategory.html",{'d':d,'date':date})

def updatecatergory(request,c_id):
    if request.method == 'POST':
        duration = request.POST.get('duration')

        catergorydb.objects.filter(id=c_id).update(Duration=duration)
        messages.success(request,"Catergory updated Succesfully!")
        return redirect(displaycatergory)

def deletecatergory(request,c_id):
    data=catergorydb.objects.filter(id=c_id)
    data.delete()
    messages.warning(request, "Catergory Deleted Succesfully!")
    return redirect(displaycatergory)


def product(request):
    date = datetime.datetime.now()
    return render(request,"addproduct.html",{'date':date})

def saveproduct(request):
    if request.method=='POST':
        product_name=request.POST.get('product_name')
        ob=productdb(Product_name=product_name)
        ob.save()
        messages.success(request,"Product Saved Succesfully!")
        return redirect(product)

def displayproduct(request):
    date = datetime.datetime.now()
    data=productdb.objects.all()
    return render(request,"displayproduct.html",{'data':data,'date':date})

def editproduct(request,w_id):
    date = datetime.datetime.now()
    d=productdb.objects.get(id=w_id)
    return render(request,"editproduct.html",{'d':d,'date':date})

def updateproduct(request,w_id):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')

        productdb.objects.filter(id=w_id).update(Product_name=product_name)
        messages.success(request,"Product Updated Succesfully!")
        return redirect(displayproduct)

def deleteproduct(request,w_id):
    data=productdb.objects.filter(id=w_id)
    data.delete()
    messages.warning(request, "Product Deleted Succesfully!")
    return redirect(displayproduct)


def addpottery(request):
    date=datetime.datetime.now()
    product=productdb.objects.all()
    return render(request,"addpotteryproduct.html",{'product':product,'date':date})

def savepottery(request):
    if request.method=='POST':
        pottery_name=request.POST.get('pottery_name')
        pottery_category=request.POST.get('pottery_category')
        pottery_price=request.POST.get('pottery_price')
        pottery_description=request.POST.get('pottery_description')
        pottery_image=request.FILES.get('pottery_image')

        ob=potterydb(Pottery_name=pottery_name,
                     Pottery_category=pottery_category,
                     Pottery_price=pottery_price,
                     Pottery_description=pottery_description,
                     Pottery_image=pottery_image)

        ob.save()
        messages.success(request,"Pottery Saved Succesfully!")
        return redirect(addpottery)

def displaypottery(request):
    date=datetime.datetime.now()
    data=potterydb.objects.all()
    return render(request,"displaypotteryproduct.html",{'data':data,'date':date})

def editpottery(request,p_id):
    date=datetime.datetime.now()
    product=productdb.objects.all()
    pottery=potterydb.objects.get(id=p_id)
    return render(request,"editpotteryproduct.html",{'pottery':pottery, 'product':product,'date':date})

def updatepottery(request,p_id):
    if request.method == 'POST':
        pottery_name = request.POST.get('pottery_name')
        pottery_category = request.POST.get('pottery_category')
        pottery_price = request.POST.get('pottery_price')
        pottery_description = request.POST.get('pottery_description')
        try:
            pottery_image = request.FILES['pottery_image']
            fs=FileSystemStorage()
            files=fs.save(pottery_image.name,pottery_image)
        except MultiValueDictKeyError:
            files=potterydb.objects.get(id=p_id).Pottery_image

        potterydb.objects.filter(id=p_id).update(Pottery_name=pottery_name,
                       Pottery_category=pottery_category,
                       Pottery_price=pottery_price,
                       Pottery_description=pottery_description,
                       Pottery_image=files)
        messages.success(request,"Pottery Updated Succesfully!")
        return redirect(displaypottery)

def deletepottery(request,p_id):
    data=potterydb.objects.filter(id=p_id)
    data.delete()
    messages.warning(request, "Pottery Deleted Succesfully!")
    return redirect(displaypottery)

def displayorder(request):
    date=datetime.datetime.now()
    data=Orderdb.objects.all()
    return render(request,"displayorder.html",{'data':data,'date':date})

def deleteorder(request,o_id):
    data=Orderdb.objects.filter(id=o_id)
    data.delete()
    messages.warning(request, "Order Deleted Succesfully!")
    return redirect(displayorder)

def displaybooking(request):
    date=datetime.datetime.now()
    data=Bookingdb.objects.all()
    return render(request,"displaybooking.html",{'data':data,'date':date})

def deletebooking(request,b_id):
    data=Bookingdb.objects.filter(id=b_id)
    data.delete()
    messages.warning(request, "Booking Deleted Succesfully!")
    return redirect(displaybooking)



def adminloginpage(request):
    return render(request,"adminpage.html")

def adminlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if User.objects.filter(username__contains=username).exists():
            data=authenticate(username=username,password=password)

            if data is not None:
                login(request,data)
                request.session['username']=username
                request.session['password']=password
                messages.success(request, "Login Succesfully!")
                return redirect(indexpage)
            else:
                messages.warning(request, "Username or password Incorrect!")
                return redirect(adminloginpage)
        else:
            messages.warning(request, "Username or password Incorrect!")
            return redirect(adminloginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Succesfully!")
    return redirect(adminloginpage)