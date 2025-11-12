from django.urls import path
from Myapp import views

urlpatterns=[
    path('index/',views.indexpage,name="index"),

    path('catergory/', views.catergory, name="catergory"),
    path('savecatergory/', views.savecatergory, name="savecatergory"),
    path('displaycatergory/', views.displaycatergory, name="displaycatergory"),
    path('editcatergory<int:c_id>/', views.editcatergory, name="editcatergory"),
    path('updatecatergory/<int:c_id>/', views.updatecatergory, name="updatecatergory"),
    path('deletecatergory/<int:c_id>/', views.deletecatergory, name="deletecatergory"),

    path('product/', views.product, name="product"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:w_id>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:w_id>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:w_id>/', views.deleteproduct, name="deleteproduct"),

    path('addpottery/',views.addpottery,name="addpottery"),
    path('savepottery/',views.savepottery,name="savepottery"),
    path('displaypottery/',views.displaypottery,name="displaypottery"),
    path('editpottery/<int:p_id>/',views.editpottery,name="editpottery"),
    path('updatepottery/<int:p_id>/',views.updatepottery,name="updatepottery"),
    path('deletepottery/<int:p_id>/',views.deletepottery,name="deletepottery"),

    path('displayorder/',views.displayorder,name="displayorder"),
    path('deleteorder/<int:o_id>/',views.deleteorder,name="deleteorder"),

    path('displaybooking/',views.displaybooking,name="displaybooking"),
    path('deletebooking/<int:b_id>/',views.deletebooking,name="deletebooking"),

    path('AdminLoginPage/', views.adminloginpage, name="AdminLoginPage"),
    path('AdminLogin/', views.adminlogin, name="AdminLogin"),
    path('AdminLogout/',views.adminlogout,name="AdminLogout"),
]