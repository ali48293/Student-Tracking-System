from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "SMS.hod_views":
                    pass
                elif modulename == "SMS.views" or modulename == "django.views.static" or modulename == "django.contrib.auth.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("hod"))
            elif user.user_type == "2":
                if modulename == "SMS.staffViews":
                    pass
                elif modulename == "SMS.views" or modulename == "django.views.static" or modulename == "django.contrib.auth.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "3":
                if modulename == "SMS.studentViews":
                    pass
                elif modulename == "SMS.views" or modulename == "django.views.static" or modulename == "django.contrib.auth.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect(reverse("login"))
                    
        
        else:
            if request.path == reverse("login") or request.path == reverse("doLogin") or modulename == "django.contrib.auth.views":
                pass
            else:
                return HttpResponseRedirect(reverse("login"))