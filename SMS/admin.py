from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,AdminHOD,Staffs,Courses,Subjects,Students,Attendance,AttendanceReport,LeaveReportStudent,LeaveReportStaffs,FeedbackStudent,FeedbackStaff,NotificationStaff,NotificationStudent

class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser,UserModel)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaffs)
admin.site.register(FeedbackStaff)
admin.site.register(FeedbackStudent)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaff)

