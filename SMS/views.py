from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,HttpResponse
from SMS.EmailBackend import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def showloginpage(request):
    return render(request,'login_page.html')

def doLogin(request):
    if request.method !="POST":
        
        return HttpResponse("<h1>Method Not Allowed!</h2")
    
    else:
        user = EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user != None:
            login(request,user)
            if user.user_type == "1":
                
                return HttpResponseRedirect("HOD/")
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "3":
                return HttpResponseRedirect( reverse("student_home"))
        else:
            messages.error(request,"Invalid Credentials!")
            return HttpResponseRedirect("/")
        
        
def GetUserDetails(request):
    if request.user != None:
        
        return HttpResponse("User: "+request.user.email+"user_Type: " + request.user.user_type)
    else:
        return HttpResponse("Please Login First!")
    
    
def logout_user(request):
    
    logout(request)
    return HttpResponseRedirect("/")