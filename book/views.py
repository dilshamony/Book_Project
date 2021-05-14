from django.shortcuts import render,redirect
from .forms import BookCreateForm
from .models import Book
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from .decorators import login_required,admin_only

#Class Base View
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy,reverse

# Create your views here.



@admin_only
def create_book(request):
    #if request.user.is_authenticated:
    context={}
    form=BookCreateForm()
    context["form"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            #bname=form.cleaned_data.get("book_name")#name in double quotes is the name given in forms.py
            #auther=form.cleaned_data.get("auther")
            #price=form.cleaned_data.get("price")
            #pages=form.cleaned_data.get("pages")
            #now creating book using models. for that use orm query for book creation
            #book=Book(book_name=bname,auther=auther,price=price,pages=pages)#book_name is from models.py and bname is from this page. similar for the others also
            #book.save()
            #print("Book is saved")
            form.save()
            return redirect("list")#list is the name in urls.py
            #else:
                #pass
    return render(request,"book/bookcreate.html",context)
    #else:
        #return redirect("userlogin")
#try to give different name(book_name,bname,....) in form models and views , so that we can understand more precisely. but its not false yo give same name. giving dfnrt nane jst for us to understand....



#to list all books
#books=Book.objects.all()

@login_required
def list_all_book(request):#this name is given in urls
    context={}
    books = Book.objects.all()
    context["books"]=books
    return render(request,"book/listallbooks.html",context)

#to get view of each book

@login_required
def book_detail(request,id):
    #if request.user.is_authenticated:
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book/bookdetail.html",context)
    #else:
        #return redirect("userlogin")


#To delete book

@admin_only
def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("list")


# to update book
#def edit_book(request,id):
#    book = Book.objects.get(id=id)
#    boook={
#        "book_name":book.book_name,
#        "auther":book.auther,
#        "price":book.price,
#        "pages":book.pages
#    }
#    form = BookCreateForm(initial=boook)
#    context = {}
#    context["form"] = form
#    if request.method == 'POST':
#        form = BookCreateForm(request.POST)
#        if form.is_valid():
#            bname = form.cleaned_data.get("book_name")  # name in double quotes is the name given in forms.py
#            auther = form.cleaned_data.get("auther")
#            price = form.cleaned_data.get("price")
#            pages = form.cleaned_data.get("pages")
#            print(bname,auther,price,pages)
#            # now creating book using models. for that use orm query for book creation
#            book.book_name=bname
#            book.auther=auther
#            book.price=price
#            book.pages=pages # book_name is from models.py and bname is from this page. similar for the others also
#            book.save()
#            return redirect("list")  # list is the name in urls.py
#        else:
#            pass
#    return render(request, "book/editbook.html", context)


# Model Form to update book

@admin_only
def edit_book(request,id):
    book = Book.objects.get(id=id)
    form = BookCreateForm(instance=book)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = BookCreateForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("list")  # list is the name in urls.py
        else:
            pass
    return render(request, "book/editbook.html", context)


#to register a user
#user(firstname,lastname,email,password phone)
#forms.py
#model form
#registration in views



#To create view of REGISTRATION
def registration(request):
    form=UserRegistrationForm
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"book/login.html")
        else:
            form=UserRegistrationForm(request.POST)
            context["form"]=form
            return redirect("userlogin")
    return render(request,"book/registration.html",context)


#LOGIN
def login_user(request):
    context={}
    form=LoginForm()
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"book/index.html")
    return render(request,"book/login.html",context)

#LOGOUT
def signout(request):
    logout(request)
    return redirect("userlogin")





                              #CLASS BASED VIEW
#-----------------------------------------------------------------------------------------------------


#LIST VIEW
class BookList(ListView):
    model=Book
    template_name = "book/listallbooks.html"
    context_object_name = "books"

#CREATE BOOK
class BookCreate(CreateView):
    model = Book
    template_name = "book/bookcreate.html"
    form_class = BookCreateForm
    success_url = reverse_lazy("books")
    #OR
    #def get_success_url(self):
     #   return reverse("books")

#DETAIL OF BOOK
class BookDetail(DetailView):
    model = Book
    template_name = "book/bookdetail.html"
    context_object_name = "book"#book is from bookdetail.html

#UPDATE BOOK
class BookUpdate(UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = "book/editbook.html"
    success_url = reverse_lazy("books")

#DELETE BOOK
class DeleteBook(DeleteView):
    model = Book
    template_name = "book/deletebook.html"
    context_object_name = "books"
    success_url = reverse_lazy("books")



#                 CUSTOMIZATION
#---------------------------------------------------

#LIST
class ListBook(TemplateView):
    model=Book
    template_name = "book/listallbooks.html"
    context={}
    def get(self,request,*args,**kwargs):
        books=self.model.objects.all()
        print(books)
        self.context["books"]=books
        return render(request,self.template_name,self.context)

#CREATE
class CreateBook(TemplateView):
    model=Book
    template_name = "book/bookcreate.html"
    context={}
    form_class=BookCreateForm
    def get(self,request,*args,**kwargs):
        self.context["form"]=self.form_class()
        return render(request,self.template_name,self.context)
    def post(self,request):
        form= self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tbooks")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)


class ObjectMixin(object):
    model=None
    def get_object(self,id):
        return self.model.objects.get(id=id)

#DETAIL
class DetailBook(TemplateView,ObjectMixin):
    model=Book
    template_name = "book/bookdetail.html"
    context={}
#    def get_object(self,id):
#        return self.model.objects.get(id=id)
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        book=self.get_object(id)
        self.context["book"]=book
        return render(request,self.template_name,self.context)

#UPDATE
class UpdateBook(TemplateView,ObjectMixin):
    model=Book
    template_name = "book/editbook.html"
    form_class=BookCreateForm
    context={}
    lookup=0
#    def get_object(self,id):
#        return self.model.objects.get(id=id)
    def get(self,request,*args,**kwargs):
        self.lookup=kwargs.get("pk")
        book = self.get_object(self.lookup)
        form=self.form_class(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,**kwargs):
        self.lookup=kwargs.get("pk")
        book=self.get_object(self.lookup)
        form=self.form_class(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("tbooks")
        else:
            self.context["form"]=form
            return render(request,self.template_name,self.context)

#DELETE
class BookDelete(TemplateView,ObjectMixin):
    model=Book
#    def get_object(self,id=id):
#        return self.model.objects.get(id=id)
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book=self.get_object(id)
        book.delete()
        return redirect("tbooks")