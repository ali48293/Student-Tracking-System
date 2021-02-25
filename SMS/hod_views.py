from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import CustomUser,Staffs,Courses,Subjects,Students,SessionYearModel
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import datetime
from .forms import AddStudentForm,EditStudentForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



def hod_view(request):
    return render(request,"index.html")

def hod_view(request):
    return render(request,"hod_template/homepage.html")

def add_staff_view(request):
    return render(request,'hod_template/add_staff.html')

def add_staff_save_view(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed!")
    else:
        username  = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name  = request.POST.get("last_name")
        email      = request.POST.get("email")
        address    = request.POST.get("address")
        password   = request.POST.get("password")

        
        try:
            user = CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request,"User has been added!")
            return HttpResponseRedirect("add_staff")
        except:
           messages.error(request,"User can't be added!")
           return HttpResponseRedirect("add_staff")
           
    return render(request,'hod_template/add_staff.html')

def add_student_view(request):
    form = AddStudentForm()
    return render(request,'hod_template/add_student.html',{'form':form})

def add_student_save_view(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed!")
    else:
        form = AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            username  = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name  = form.cleaned_data["last_name"]
            email      = form.cleaned_data["email"]
            address    = form.cleaned_data["address"]
            password   = form.cleaned_data["password"]
            session_id = form.cleaned_data["session_id"]
            course_id = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]
            #! profile_pic
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url = fs.url(filename)
            try:
                
                user = CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,user_type=3)
                user.students.address = address
                course_obj = Courses.objects.get(id=course_id)
                user.students.course_id =course_obj
                user.students.gender =gender
                session = SessionYearModel.objects.get(id=session_id)
                user.students.session_year_id = session
                user.students.profile_pic = profile_pic_url
                user.save()
                messages.success(request,"Student has been added!")
                return HttpResponseRedirect("add_student")
            except:
                messages.error(request,"Student can't be added!")
                return HttpResponseRedirect("add_student")
        else:
            form = AddStudentForm()
            return render(request,'hod_template/add_student.html',{'form':form})   



def add_course_view(request):
    return render(request,"hod_template/add_course.html")

def add_course_save_view(request):
     
    if request.method != "POST":
        return HttpResponse("Method is Invalid!")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request,"Successfully added the Course!")
            return HttpResponseRedirect("add_course")
        except:
            messages.error(request,"Failed to add the Course!")
            return HttpResponseRedirect("add_course")

def add_subject_view(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request,"hod_template/add_subject.html",{"courses":courses,"staffs":staffs})

def add_subject_save_view(request):
     
    if request.method != "POST":
        return HttpResponse("Method is Invalid!")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)
         
        try:
            subject_model = Subjects(subject_name=subject_name,course_id=course,staff_id=staff)
            subject_model.save()
            messages.success(request,"Successfully added the Subject!")
            return HttpResponseRedirect("add_subject")
        except:
            messages.error(request,"Failed to add the Subject!")
            return HttpResponseRedirect("add_subject")

def manage_staff_view(request):
    staffs = Staffs.objects.all().order_by("-id")
    return render(request,"hod_template/manage_Staff.html",{"staffs":staffs})

def manage_student_view(request):
    
    students = Students.objects.all().order_by("-id")
 
#! Pagination   

    page_num = int(request.GET.get('page',1))
    paginator = Paginator(students,3)
    last_Page = paginator.page_range[-1]
    try:
        page = paginator.page(page_num)
        
    except EmptyPage:
        
        page = paginator.page(1)

    return render(request,"hod_template/manage_Student.html",{"students":page,"last_Page":last_Page})

def manage_course_view(request):
    courses = Courses.objects.all()
    return render(request,"hod_template/manage_course.html",{"courses":courses})

def manage_subjects_view(request):
    subjects = Subjects.objects.all()
    return render(request,"hod_template/manage_subject.html",{"subjects":subjects})

def edit_staff_view(request,staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(request,"hod_template/edit_staff.html",{"staff":staff,"id":staff_id})

def edit_staff_save_view(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed!</h2>")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
        
            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()
            messages.success(request,"Successfully Edited the Staff!")
            return HttpResponseRedirect("edit_staff/" +staff_id)
        except:
            messages.error(request,"Failed to Edit!")
            return HttpResponseRedirect("edit_staff/"+ staff_id)




def edit_student_view(request,student_id):
    request.session['student_id'] =student_id
    
    student = Students.objects.get(admin=student_id)
    form = EditStudentForm()
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['username'].initial = student.admin.username
    form.fields['address'].initial = student.address
    form.fields['gender'].initial = student.gender
    form.fields['course'].initial = student.course_id.id
    form.fields['session_id'].initial = student.session_year_id
    form.fields['profile_pic'].initial = student.profile_pic
    form.fields['email'].initial = student.admin.email
    return render(request,"hod_template/edit_student.html",{'form':form,"id":student_id})
    

def edit_student_save_view(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed!</h2>")
    else:
        student_id = request.session.get("student_id")
        if student_id is None:
            return HttpResponse("/manage_student")
        form = EditStudentForm(request.POST,request.FILES)
        if form.is_valid():
            username  = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name  = form.cleaned_data["last_name"]
            email      = form.cleaned_data["email"]
            address    = form.cleaned_data["address"]
            session_id = form.cleaned_data["session_id"]
            course_id = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]
            
            if request.FILES.get('profile_pic',False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url = fs.url(filename)        
            else:
                profile_pic_url=None
        
        
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
        
            student_model = Students.objects.get(admin=student_id)
            student_model.address = address
            session = SessionYearModel.objects.get(id=session_id)
            student_model.session_year_id = session
            student_model.gender = gender

            course = Courses.objects.get(id= course_id)
            student_model.course_id = course
            if profile_pic_url != None:
                student_model.profile_pic = profile_pic_url
            student_model.save()
            messages.success(request,"Successfully Edited the Student!")
            return HttpResponseRedirect("edit_student/" + student_id)
            # messages.error(request,"Failed to Edit!")
            # return HttpResponseRedirect("/edit_student/" + student_id)
        else:
            form = EditStudentForm(request.POST)

            return render(request,"hod_template/edit_student.html",{'form':form,"id":student_id})
            
def edit_subject_view(request,subject_id):
    subject = Subjects.objects.get(id=subject_id)
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2) 
    return render(request,"hod_template/edit_subject.html",{"subject":subject,"courses":courses,"staffs":staffs,"id":subject_id})

def edit_subject_save_view(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method is Invalid!</h2>")
    else:
        subject_name = request.POST.get("subject_name")
        subject_id = request.POST.get("subject_id")
        staff_id = request.POST.get("staff")
        course_id = request.POST.get("course")
         
        try:
            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name = subject_name
            staff = CustomUser.objects.get(id=staff_id)
            subject.staff_id = staff
            course = Courses.objects.get(id= course_id)
            subject.course_id = course
            
            subject.save()           
            messages.success(request,"Successfully Edited the Subject!")
            return HttpResponseRedirect("edit_subject/" + subject_id)
        except:
            messages.error(request,"Failed to Edit the Subject!")
            return HttpResponseRedirect("edit_subject/" + subject_id)


def edit_course_view(request,course_id):
    course = Courses.objects.get(id=course_id)
    return render(request,"hod_template/edit_course.html",{"course":course,"id":course_id})

def edit_course_save_view(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method is Invalid!</h2>")
    else:
        course_name = request.POST.get("course")
        course_id = request.POST.get("course_id")

         
        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()           
            messages.success(request,"Successfully Edited the Course!")
            return HttpResponseRedirect("edit_course/" + course_id)
        except:
            messages.error(request,"Failed to Edit the Course!")
            return HttpResponseRedirect("edit_course/" + course_id)
    


def manage_session(request):
    return render(request,"hod_template/session_template.html")

def add_session_save(request):
    if request.method != "POST":
        return HttpResponse("reverse")
    else:
        session_start   = request.POST.get("session_start")
        session_end     = request.POST.get("session_end")
        print(session_start)
        print(session_end)
        try: 
            sessionYear = SessionYearModel(session_start_year=session_start,session_end_year=session_end)
            sessionYear.save()
            
            messages.success(request,"Successfully Added the Session!")
            return redirect("manage_session")
        except:
            messages.error(request,"Failed to Add the Session!")
            return redirect("manage_session")    