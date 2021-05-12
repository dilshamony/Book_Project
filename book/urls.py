"""bookproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import create_book,list_all_book,book_detail,delete_book,edit_book,registration,login_user,signout,\
    BookList,BookCreate,BookDetail,BookUpdate,DeleteBook

urlpatterns = [
    path("bookcreate",create_book,name="createbook"),
    path("list",list_all_book,name="list"),
    path("detail/<int:id>",book_detail,name="detail"),
    path("delete/<int:id>",delete_book,name="deletebook"),
    path("edit/<int:id>", edit_book, name="editbook"),
    path("registration",registration,name="register"),
    path("login",login_user,name="userlogin"),
    path("logout",signout,name="signout"),
    path("books",BookList.as_view(),name="books"),
    path("createbook",BookCreate.as_view(),name="bookcreate"),
    path("books/<int:pk>",BookDetail.as_view(),name="bookdetail"),
    path("books/edit/<int:pk>",BookUpdate.as_view(),name="bookedit"),
    path("deletebook/<int:pk>",DeleteBook.as_view(),name="bookdelete")
]
