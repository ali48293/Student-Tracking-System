"""StudentManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from SMS import views,hod_views,staffViews,studentViews
from StudentManagement import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("django.contrib.auth.urls")),
    path('', views.showloginpage,name='login'),
    path('doLogin', views.doLogin,name="doLogin"),
    path('logout_user/', views.logout_user),
    #! HOD
    
    path('HOD/', hod_views.hod_view, name="hod"),
    # path('HOD/', hod_views.homepageView, name="homepage"),
    path('add_staff/', hod_views.add_staff_view,name = "add_staff"),
    path('add_staff_save', hod_views.add_staff_save_view,name = "add_staff_save"),
    path('add_course', hod_views.add_course_view,name = "add_course"),
    path('add_course_save', hod_views.add_course_save_view,name = "add_course_save"),
    path('add_student', hod_views.add_student_view,name = "add_student"),
    path('add_student_save', hod_views.add_student_save_view,name = "add_student_save"),
    path('add_subject', hod_views.add_subject_view,name = "add_subject"),
    path('add_subject_save', hod_views.add_subject_save_view,name = "add_subject_save"),
    path('manage_staff', hod_views.manage_staff_view,name = "manage_staff"),
    path('manage_student', hod_views.manage_student_view,name = "manage_student"),
    path('manage_course', hod_views.manage_course_view,name = "manage_course"),
    path('manage_subjects', hod_views.manage_subjects_view,name = "manage_subjects"),
    path('edit_staff/<str:staff_id>', hod_views.edit_staff_view,name = "edit_staff"),
    path('edit_staff_save', hod_views.edit_staff_save_view,name = "edit_staff_save"),
    path('edit_student/<str:student_id>', hod_views.edit_student_view,name = "edit_student"),
    path('edit_student_save', hod_views.edit_student_save_view,name = "edit_student_save"),
    path('edit_subject/<str:subject_id>', hod_views.edit_subject_view,name = "edit_subject"),
    path('edit_subject_save', hod_views.edit_subject_save_view,name = "edit_subject_save"),
    path('edit_course/<str:course_id>', hod_views.edit_course_view,name = "edit_course"),
    path('edit_course_save', hod_views.edit_course_save_view,name = "edit_course_save"),
    path('manage_session', hod_views.manage_session,name = "manage_session"),
    path('add_session_save', hod_views.add_session_save,name = "add_session_save"),
    
    #! Staff
    
    path('staff_home', staffViews.staff_home_view,name = "staff_home"),
    path('staff_home', staffViews.staff_home_view,name = "staff_home"),
    path('update_staff/<str:staff_id>', staffViews.update_staff_view,name = "update_staff"),
    path('update_staff_save', staffViews.update_staff_save_view,name = "update_staff_save"),
    path('staff_attandence', staffViews.staff_attandence,name = "staff_attandence"),
    path('save_attandence_data', staffViews.save_attandence_data,name = "save_attandence_data"),
    path('get_students', staffViews.get_students,name = "get_students"),
    path('staff_apply_leave', staffViews.staff_apply_leave,name = "staff_apply_leave"),
    path('staff_apply_leave_save', staffViews.staff_apply_leave_save,name = "staff_apply_leave_save"),
    path('staff_feedback', staffViews.staff_feedback,name = "staff_feedback"),
    path('staff_feedback_save', staffViews.staff_feedback_save,name = "staff_feedback_save"),
 
    #! Student
    
    path('student_home', studentViews.student_home_view,name = "student_home"),
    path('student_apply_leave', studentViews.student_apply_leave,name = "student_apply_leave"),
    path('student_apply_leave_save', studentViews.student_apply_leave_save,name = "student_apply_leave_save"),
    path('student_feedback', studentViews.student_feedback,name = "student_feedback"),
    path('student_feedback_save', studentViews.student_feedback_save,name = "student_feedback_save"),
    # path('student_feedback_delete/<int:id>/', studentViews.student_feedback_del,name = "delete"),
    # path('get_user_details/',views. GetUserDetails),
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
