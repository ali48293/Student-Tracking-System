from django import forms
from SMS.models import Courses,SessionYearModel

class DateInput(forms.DateInput):
    input_type = 'date'
class AddStudentForm(forms.Form):
    
    first_name = forms.CharField(label="First Name", max_length=55,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(label="Last Name", max_length=55,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    username = forms.CharField(label="User Name", max_length=55,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    email = forms.EmailField(label="Email", max_length=55,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    address = forms.CharField(label="Address", max_length=55,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    password = forms.CharField(label="Password", max_length=55,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    gender_choice =(
        ('Male',"Male"),
        ('Female',"Female")
    )
    gender = forms.ChoiceField(label="Gender",choices=gender_choice,widget=forms.Select(attrs={'class':'form-control'}))
    courses = Courses.objects.all()
    course_list=[]
    # try:
    for course in courses :
        eachCourse = (course.id,course.course_name)
        course_list.append(eachCourse)
# except:
    # course_list=[]
    sessions = SessionYearModel.objects.all()
    session_list=[]
# try:
    for session in sessions :
        eachSession = (session.id,str(session.session_start_year) + " To " + str(session.session_end_year))
        session_list.append(eachSession)
# except:
    # course_list=[]
    course = forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={'class':'form-control'}))
    profile_pic = forms.FileField(label="Profile Pic",widget=forms.FileInput(attrs={'class':'form-control'}))
    session_id = forms.ChoiceField(label="Session Year",choices=session_list,widget=forms.Select(attrs={'class':'form-control'}))
    
class EditStudentForm(forms.Form):
    
    first_name = forms.CharField(label="First Name", max_length=55,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Last Name", max_length=55,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label="User Name", max_length=55,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Email", max_length=55,widget=forms.EmailInput(attrs={'class':'form-control'}))
    address = forms.CharField(label="Address", max_length=55,widget=forms.TextInput(attrs={'class':'form-control'}))
    gender_choice =(
        ('Male',"Male"),
        ('Female',"Female")
    )
    gender = forms.ChoiceField(label="Gender",choices=gender_choice,widget=forms.Select(attrs={'class':'form-control'}))
    courses = Courses.objects.all()
    course_list=[]
    try:
        for course in courses :
            eachCourse = (course.id,course.course_name)
            course_list.append(eachCourse)
    except:
        course_list=[]
    sessions = SessionYearModel.objects.all()
    session_list=[]
# try:
    for session in sessions :
        eachSession = (session.id,str(session.session_start_year) + " To " + str(session.session_end_year))
        session_list.append(eachSession)
    
    course = forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={'class':'form-control'}))
    profile_pic = forms.FileField(label="Profile Pic",widget=forms.FileInput(attrs={'class':'form-control'}))
    session_id = forms.ChoiceField(label="Session Year",choices=session_list,widget=forms.Select(attrs={'class':'form-control'}))
    
    