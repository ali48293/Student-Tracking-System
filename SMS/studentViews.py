from django.shortcuts import render
from .models import Students,LeaveReportStudent,FeedbackStudent
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Students
def student_home_view(request):
    
    return render(request,"student_template/student_home.html")
def student_home_view(request):
    
    return render(request,"student_template/homepage.html")
# def student_update_view(request):
#     student = Students.objects.get(admin=request.usr.)
    return render(request,"student_template/homepage.html")

def student_apply_leave(request):
    staff_obj = Students.objects.get(admin=request.user.id)
    
    all_obj = LeaveReportStudent.objects.filter(student_id=staff_obj)
    return render(request,'student_template/student_leave.html',{"leave_reports":all_obj})

def student_apply_leave_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Valid")
    else:
        leave_date   =  request.POST.get("leave_date")
        leave_reason =  request.POST.get("leave_reason")
        staff_obj = Students.objects.get(admin=request.user.id)
        # try: 
        LeaveReportStudent.objects.create(student_id= staff_obj,leave_date=leave_date,leave_message=leave_reason,leave_status=0)
       
        messages.success(request,"Leave Has been delivered!")
        return HttpResponseRedirect("student_apply_leave")
        # except:
        #     messages.error(request,"Failed to send the leave!")
        #     return HttpResponseRedirect("student_apply_leave")


def student_feedback(request):
    staff_obj = Students.objects.get(admin=request.user.id)
    
    all_obj = FeedbackStudent.objects.filter(student_id=staff_obj)
    return render(request,'student_template/student_feedback.html',{"leave_reports":all_obj})

def student_feedback_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Valid")
    else:
        feedback   =  request.POST.get("feedback")

        staff_obj = Students.objects.get(admin=request.user.id)
        try: 
            feedback_report=FeedbackStudent(student_id=staff_obj,feedback= feedback,feedback_reply="")
            feedback_report.save()
            messages.success(request,"Feedback Has been delivered!")
            return HttpResponseRedirect("student_feedback")
        except:
            messages.error(request,"Failed to send the Feedback!")
            return HttpResponseRedirect("student_feedback")


