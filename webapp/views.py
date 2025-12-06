from django.shortcuts import render, redirect
from Myapp.models import productdb, potterydb, catergorydb
from webapp.models import Signupdb, Bookingdb, Orderdb,Cartdb
from django.contrib import messages


# Create your views here.
def Homepage(request):
    product = productdb.objects.all()
    return render(request, "Homepage.html", {'product': product})


def Contactpage(request):
    product = productdb.objects.all()
    return render(request, "Contactpage.html", {'product': product})


def Bookingpage(request):
    product = productdb.objects.all()
    duration = catergorydb.objects.all()
    return render(request, "Bookingpage.html", {'product': product, 'duration': duration})

def Legacygpage(request):
    product = productdb.objects.all()
    return render(request, "Legacypage.html", {'product': product})


def Workshoppage(request):
    product = productdb.objects.all()
    return render(request, "Workshoppage.html", {'product': product})


def Creationpage(request):
    product = productdb.objects.all()
    return render(request, "Creationpage.html", {'product': product})


def Orderpage(request):
    product = productdb.objects.all()
    return render(request, "Orderpage.html", {'product': product})


def Cartpage(request):
    product = productdb.objects.all()
    cart=Cartdb.objects.all()
    return render(request, "Cartpage.html", {'product': product,'cart':cart})


def Categorypage(request, product_name):
    product = productdb.objects.all()
    pottery = potterydb.objects.filter(Pottery_category=product_name)
    return render(request, "Categorypage.html.", {'product': product, 'pottery': pottery, 'product_name': product_name})


def Singleproductpage(request, pottery_id):
    pottery = potterydb.objects.get(id=pottery_id)
    product = productdb.objects.all()
    return render(request, "singleproduct.html", {'pottery': pottery, 'product': product})


def savebooking(request):
    if request.method == 'POST':
        book_first = request.POST.get('book_first')
        book_last = request.POST.get('book_last')
        book_age = request.POST.get('book_age')
        gender = request.POST.get('gender')
        book_address = request.POST.get('book_address')
        book_mobile = request.POST.get('book_mobile')
        book_email = request.POST.get('book_email')
        book_class = request.POST.get('book_class')

        ob = Bookingdb(Booking_firstname=book_first,
                       Booking_lastname=book_last,
                       Booking_age=book_age,
                       Booking_gender=gender,
                       Booking_address=book_address,
                       Booking_email=book_email,
                       Booking_mobile=book_mobile,
                       Booking_class=book_class)

        ob.save()
        messages.success(request,"Booked Successfully!")
        return redirect(Bookingpage)


def saveorder(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment = request.POST.get('payment')

        ob = Orderdb(Order_fullname=fullname,
                     Order_email=email,
                     Order_phone=phone,
                     Order_address=address,
                     Order_payment=payment)

        ob.save()
        messages.success(request,"Order Placed Successfully!")
        return redirect(Orderpage)

def savecart(request):
    if request.method=='POST':
        singlepottery_quantity=request.POST.get('singlepottery_quantity')
        singlepottery_price=request.POST.get('singlepottery_price')
        singlepottery_total=request.POST.get('singlepottery_total')
        singlepottery_name=request.POST.get('singlepottery_name')
        singlepottery_username=request.POST.get('singlepottery_username')
        pottery=potterydb.objects.filter(Pottery_name=singlepottery_name).first()
        singlepottery_image=pottery.Pottery_image
        potteryid=pottery.id

        ob=Cartdb(Singlepottery_username=singlepottery_username,
                  Singlepottery_name=singlepottery_name,
                  Singlepottery_price=singlepottery_price,
                  Singlepottery_total=singlepottery_total,
                  Singlepottery_quantity=singlepottery_quantity,
                  Singlepottery_image=singlepottery_image,
                  Potteryid=potteryid)
        ob.save()
        messages.success(request,"Added To Cart!")
        return redirect(Homepage)

def deletecart(request,c_id):
    data=Cartdb.objects.filter(id=c_id).delete()
    return redirect(Cartpage)


def Checkoutpage(request):
    product = productdb.objects.all()
    return render(request, "Checkoutpage.html", {'product': product})


def usersignup(request):
    return render(request, "Usersignup.html")

def Signupdisplay(request):
    data=Signupdb.objects.all()
    return render(request,"signupdisplay.html",{'data':data})

def Deletesignup(request,s_id):
    data=Signupdb.objects.filter(id=s_id)
    data.delete()
    return redirect(Signupdisplay)


def userlogin(request):
    return render(request, "Userlogin.html")


def saveusersignup(request):
    if request.method == 'POST':
        signup_username = request.POST.get('signup_username')
        signup_email = request.POST.get('signup_email')
        signup_mobile = request.POST.get('signup_mobile')
        signup_password = request.POST.get('signup_password')
        signup_confirm = request.POST.get('signup_confirm')

        ob = Signupdb(Signup_username=signup_username,
                      Signup_email=signup_email,
                      Signup_mobile=signup_mobile,
                      Signup_password=signup_password,
                      Signup_confirm=signup_confirm)

        if Signupdb.objects.filter(Signup_username=signup_username).exists():
            messages.warning(request, "Username already exists!")
            return redirect(usersignup)
        elif Signupdb.objects.filter(Signup_email=signup_email).exists():
            messages.warning(request, "Email already exists!")
            return redirect(usersignup)
        elif Signupdb.objects.filter(Signup_mobile=signup_mobile).exists():
            messages.warning(request, "Mobile Number already exists!")
            return redirect(usersignup)
        else:
            ob.save()
            messages.success(request, "Signup Successfully!")
            return redirect(userlogin)


def login(request):
    if request.method == 'POST':
        login_username = request.POST.get('login_username')
        login_password = request.POST.get('login_password')

        if Signupdb.objects.filter(Signup_username=login_username, Signup_password=login_password).exists():
            request.session['username'] = login_username
            messages.success(request, "Login Successfully!")
            return redirect(Homepage)
        else:
            messages.warning(request, "Incorrect username or password!")
            return redirect(userlogin)
    else:
        messages.warning(request, "Try Again!")
        return redirect(userlogin)


def logout(request):
    del request.session['username']
    messages.success(request, "Logout Successfully!")
    return redirect(userlogin)
