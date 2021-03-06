from django.shortcuts import redirect

def login_required(func):
    def wrapper(request,*args,**kwargs): #request is the argument. bt in details there iare 2 arguments request and id, so there is a chance that we have many more aeguments. so using *args and **kwargs
        if not request.user.is_authenticated:
            return redirect("userlogin")
        return func(request,*args,**kwargs)
    return wrapper


def admin_only(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect("userlogin")
        return func(request,*args,**kwargs)
    return wrapper