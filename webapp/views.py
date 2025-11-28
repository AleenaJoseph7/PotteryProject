from django.shortcuts import render, redirect
from Myapp.models import productdb, potterydb, catergorydb
from webapp.models import Signupdb, Bookingdb, Orderdb


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
    return render(request, "Cartpage.html", {'product': product})


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
        return redirect(Orderpage)


def Checkoutpage(request):
    product = productdb.objects.all()
    return render(request, "Checkoutpage.html", {'product': product})


def usersignup(request):
    return render(request, "Usersignup.html")


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
            return redirect(usersignup)
        elif Signupdb.objects.filter(Signup_email=signup_email).exists():
            return redirect(usersignup)
        elif Signupdb.objects.filter(Signup_mobile=signup_mobile).exists():
            return redirect(usersignup)
        else:
            ob.save()
            return redirect(userlogin)


def login(request):
    if request.method == 'POST':
        login_username = request.POST.get('login_username')
        login_password = request.POST.get('login_password')

        if Signupdb.objects.filter(Signup_username=login_username, Signup_password=login_password).exists():
            request.session['username'] = login_username
            request.session['password'] = login_password
            return redirect(Homepage)
        else:
            return redirect(userlogin)
    else:
        return redirect(userlogin)


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(userlogin)
