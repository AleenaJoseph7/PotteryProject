from django.urls import path
from webapp import views

urlpatterns = [
    path('Homepage', views.Homepage, name="Homepage"),
    path('Contactpage', views.Contactpage, name="Contactpage"),
    path('Bookingpage', views.Bookingpage, name="Bookingpage"),
    path('Legacygpage', views.Legacygpage, name="Legacygpage"),
    path('Workshoppage', views.Workshoppage, name="Workshoppage"),
    path('Creationpage', views.Creationpage, name="Creationpage"),
    path('Orderpage', views.Orderpage, name="Orderpage"),
    path('Cartpage', views.Cartpage, name="Cartpage"),
    path('Categorypage/<product_name>/', views.Categorypage, name="Categorypage"),
    path('Singleproductpage/<int:pottery_id>/', views.Singleproductpage, name="Singleproductpage"),
    path('saveorder/', views.saveorder, name="saveorder"),
    path('savebooking/', views.savebooking, name="savebooking"),

    path('Checkoutpage/', views.Checkoutpage, name="Checkoutpage"),
    path('savecheckout/', views.savecheckout, name="savecheckout"),
    path('editcheckout/', views.editcheckout, name="editcheckout"),
    path('deletecheckout/<int:d_id>/', views.deletecheckout, name="deletecheckout"),
    path('PaymentPage/', views.PaymentPage, name="PaymentPage"),

    path('savecart/', views.savecart, name="savecart"),
    path('deletecart/<int:c_id>/', views.deletecart, name="deletecart"),

    path('userlogin/', views.userlogin, name="userlogin"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('saveusersignup/', views.saveusersignup, name="saveusersignup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    path('Signupdisplay/', views.Signupdisplay, name="Signupdisplay"),
    path('Deletesignup/<int:s_id>/', views.Deletesignup, name="Deletesignup"),
]
