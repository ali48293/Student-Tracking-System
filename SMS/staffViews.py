from django.shortcuts import render,redirect
from SMS.models import Subjects,SessionYearModel,Students
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
import json
from django.contrib import messages
from .models import LeaveReportStaffs,Staffs,FeedbackStaff,CustomUser
def staff_home_view(request):
    return render(request,"staff_template/staff_home.html")
def staff_home_view(request):
    # course = Subjects.objects.filter(staff_id=21)
    staff = Staffs.objects.get(admin=request.user.id)
    Subs = Subjects.objects.filter(staff_id=request.user.id)
    return render(request,"staff_template/homepage.html",{'Subjects':Subs,"staff":staff})

def update_staff_view(request,staff_id):
    staffs = Staffs.objects.get(admin=staff_id)
    # print(staff)
    return render(request,"staff_template/edit_staff.html",{"staff":staffs,"id":staff_id})

def update_staff_save_view(request):
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




def staff_attandence(request):
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    sessions =  SessionYearModel.objects.all()
    return render(request,"staff_template/staff_attandence.html",{"subjects":subjects,"sessions":sessions})


@csrf_exempt
def get_students(request):
    
    subject_id = request.POST.get("subject")
    session_year = request.POST.get("session_year")
    
    subject = Subjects.objects.get(id=subject_id)
    session = SessionYearModel.objects.get(id=session_year)
    students = Students.objects.filter(course_id=subject.course_id,session_year_id=session)
    list_data=[]
    for student in students:
        eachStudent = {"id":student.admin.id,'name':student.admin.first_name + ' '+ student.admin.last_name }
        list_data.append(eachStudent)
    return JsonResponse(json.dumps(list_data),content_type='applicaiton/json',safe=False)

def staff_apply_leave(request):
    staff_obj = Staffs.objects.get(admin=request.user.id)
    
    all_obj = LeaveReportStaffs.objects.filter(staff_id=staff_obj)
    return render(request,'staff_template/staff_leave.html',{"leave_reports":all_obj})

def staff_apply_leave_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Valid")
    else:
        leave_date   =  request.POST.get("leave_date")
        leave_reason =  request.POST.get("leave_reason")
        staff_obj = Staffs.objects.get(admin=request.user.id)
        try: 
            leave_report=LeaveReportStaffs(staff_id= staff_obj,leave_date=leave_date,leave_message=leave_reason,leave_status=0)
            leave_report.save()
            messages.success(request,"Leave Has been delivered!")
            return HttpResponseRedirect("staff_apply_leave")
        except:
            messages.error(request,"Failed to send the leave!")
            return HttpResponseRedirect("staff_apply_leave")


def staff_feedback(request):
    staff_obj = Staffs.objects.get(admin=request.user.id)
    
    all_obj = FeedbackStaff.objects.filter(staff_id=staff_obj)
    return render(request,'staff_template/feedback.html',{"leave_reports":all_obj})

def staff_feedback_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Valid")
    else:
        feedback   =  request.POST.get("feedback")

        staff_obj = Staffs.objects.get(admin=request.user.id)
        try: 
            feedback_report=FeedbackStaff(staff_id=staff_obj,feedback= feedback,feedback_reply="")
            feedback_report.save()
            messages.success(request,"Feedback Has been delivered!")
            return HttpResponseRedirect("staff_feedback")
        except:
            messages.error(request,"Failed to send the Feedback!")
            return HttpResponseRedirect("staff_feedback")
