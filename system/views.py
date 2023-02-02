import datetime, os
from xml.etree.ElementTree import tostring
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.conf import settings
from sklearn.model_selection import train_test_split
from sklearn import model_selection, preprocessing
import pickle 
import pandas as pd
from pyearth import Earth

# Create your views here.
def landingpage(request):
    # pred = ''
    # divshow = False
    # if 'result' not in request.session:
    #     divshow = True
    # else:
    #     pred = request.session['result']

    context = {
        'page':'landingpage',
        # 'predict':pred,
        # 'divshow':divshow,
    }
    return render(request, 'landingpage.html', context)

def test_result(request):
    pred = ''
    divshow = False
    if 'result' not in request.session:
        divshow = True
    else:
        studid = Student.objects.get(id=request.session['id'])
        pred = request.session['result']
        if request.method == 'POST':
            if request.POST.get('shiftDecision') == "1":
                studid.shiftDecision = 1
            elif request.POST.get('shiftDecision') == "2":
                studid.shiftDecision = 0
            studid.save()
            return redirect('landingpage')
    context = {
        'page':'landingpage',
        'predict':pred,
        # 'studid':studid,
        'divshow':divshow
    }
    return render(request, 'test_result.html', context)

def about(request):
    context = {
        'page':'about'
    }
    return render(request, 'about.html', context)
def framework(request):
    context = {
        'page':'framework'
    }
    return render(request, 'framework.html', context)
def test(request):
    cet = [
        ('BS Information and Technology','BS Information and Technology'),
        ('BS Computer Science','BS Computer Science'),
        ('BS Chemical Engineering (BSCHE)','BS Chemical Engineering (BSCHE)'),
        ('BS Civil Engineering (BSCE)','BS Civil Engineering (BSCE)'),
        ('BS Computer Engineering (BSCpE)','BS Computer Engineering (BSCpE)'),
        ('BS Electrical Engineering (BSEE)','BS Electrical Engineering (BSEE)'),
        ('BS Electronics Engineering (BSECE)','BS Electronics Engineering (BSECE)'),
        ('BS Mechanical Engineering (BSME)','BS Mechanical Engineering (BSME)'),
        ('BS Manufacturing Engineering (BSMfgE)','BS Manufacturing Engineering (BSMfgE)'),
    ]
    plmbs = [
        ('Bachelor of Science in Accountancy (BSA)','Bachelor of Science in Accountancy (BSA)'),
        ('Bachelor of Science in Business Administration major in Financial Management (BSBA FM)','Bachelor of Science in Business Administration major in Financial Management (BSBA FM)'),
        ('Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)','Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)'),
        ('Bachelor of Science in Business Administration major in Operations Management (BSBA OM)','Bachelor of Science in Business Administration major in Operations Management (BSBA OM)'),
        ('Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)','Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)'),
        ('Bachelor of Science in Business Administration major in Business Economics(BSBA BE)','Bachelor of Science in Business Administration major in Business Economics(BSBA BE)'),
        ('Bachelor of Science in Entrepreneurship (BS ENTRE)','Bachelor of Science in Entrepreneurship (BS ENTRE)'),
        ('Bachelor of Science in Real Estate Management (BSREM)','Bachelor of Science in Real Estate Management (BSREM)'),
        ('Bachelor of Science in Hospitality Management (BSHM)','Bachelor of Science in Hospitality Management (BSHM)'),
        ('Bachelor of Science in Tourism Management (BSTM)','Bachelor of Science in Tourism Management (BSTM)'),
    ]
    arch = [
        ('Bachelor of Science in Architecture - BS Arch','Bachelor of Science in Architecture - BS Arch'),
    ]
    ced = [
        ('Bachelor of Elementary Education (Generalist) (BEEd)','Bachelor of Elementary Education (Generalist) (BEEd)'),
        ('Bachelor of Secondary Education major in English (BSEd-Eng)','Bachelor of Secondary Education major in English (BSEd-Eng)'),
        ('Bachelor of Secondary Education major in Filipino (BSEd-Fil)','Bachelor of Secondary Education major in Filipino (BSEd-Fil)'),
        ('Bachelor of Secondary Education major Mathematics (BSEd-Math)','Bachelor of Secondary Education major Mathematics (BSEd-Math)'),
        ('Bachelor of Secondary Education major in Sciences (BSEd-Sciences)','Bachelor of Secondary Education major in Sciences (BSEd-Sciences)'),
        ('Bachelor of Secondary Education major in Social Studies (BSEd-SS)','Bachelor of Secondary Education major in Social Studies (BSEd-SS)'),
        ('Bachelor of Physical Education (BPE)','Bachelor of Physical Education (BPE)'),
    ]
    chass = [
        ('Bachelor of Arts in Communication - BAC','Bachelor of Arts in Communication - BAC'),
        ('Bachelor of Arts in Communication Major in Public Relations - BAC-PR','Bachelor of Arts in Communication Major in Public Relations - BAC-PR'),
        ('Bachelor of Arts in Public Relations - BAPR','Bachelor of Arts in Public Relations - BAPR'),
        ('Bachelor of Science in Social Work - BS SW','Bachelor of Science in Social Work - BS SW'),
    ]
    cpt = [
        ('Bachelor of Science in Physical Therapy - BSPT','Bachelor of Science in Physical Therapy - BSPT'),
    ]
    cn = [
        ('Bachelor of Science in Nursing - BSN','Bachelor of Science in Nursing - BSN'),
    ]
    cs = [
        ('Bachelor of Science in Biology - BS Bio','Bachelor of Science in Biology - BS Bio'),
        ('Bachelor of Science in Psychology - BS PSY','Bachelor of Science in Psychology - BS PSY'),
        ('Bachelor of Science in Chemistry - BS Chem','Bachelor of Science in Chemistry - BS Chem'),
        ('Bachelor of Science in Mathematics - BS Math','Bachelor of Science in Mathematics - BS Math'),
    ]

    context = {
        'page':'test',
        'course':Student.course,
        'gwa':Student.gwa,
        'strand':Student.strand,
        'no_of_stud':Student.no_of_stud,
        'who_decided':Student.who_decided,
        'who_influenced':Student.who_influcenced,
        'year':Student.year,
        'department':CustomUser.department_list,
        'cet': cet,
        'plmbs':plmbs,
        'arch':arch,
        'ced':ced,
        'chass':chass,
        'cpt':cpt,
        'cn':cn,
        'cs':cs,
    }
    # model = pd.read_pickle('mars_model.pickle')
    xtrain = Student.objects.values_list('decision_making1', 'decision_making2', 'decision_making3', 'decision_making4','decision_making5', 'personal_assessment1', 'personal_assessment2', 'personal_assessment3', 'personal_assessment4', 'personal_assessment5', 'course_enviroment1', 'course_enviroment2', 'course_enviroment3', 'course_enviroment4','course_enviroment5', 'course_satisfaction1', 'course_satisfaction2', 'course_satisfaction3', 'course_satisfaction4', 'course_satisfaction5','academic_experience1', 'academic_experience2', 'academic_experience3', 'academic_experience4', 'academic_experience5')
    ytrain = Student.objects.values_list('shiftDecision')
    # row = [[3,3,4,4,2,2,2,2,2,2,3,3,3,3,1,2,2,2,3,2,2,2,2,4,3]]
    # xdict = pd.read_pickle('X_train.pickle')
    # ydict = pd.read_pickle('y_train.pickle')
    # adf = pd.DataFrame(a, columns =['Decision_Making1', 'Decision_Making2', 'Decision_Making3', 'Decision_Making4','Decision_Making5', 'Personal_Assessment1', 'Personal_Assessment2', 'Personal_Assessment3', 'Personal_Assessment4', 'Personal_Assessment5', 'Course_Environment1', 'Course_Environment2', 'Course_Environment3', 'Course_Environment4','Course_Environment5', 'Course_Satisfaction1', 'Course_Satisfaction2', 'Course_Satisfaction3', 'Course_Satisfaction4', 'Course_Satisfaction5','Academic_Experience1', 'Academic_Experience2', 'Academic_Experience3', 'Academic_Experience4', 'Academic_Experience5'])

    # xtrain = pd.concat([xdict, df2], ignore_index = True)
    
    #X_train, X_test, y_train, y_test = model_selection.train_test_split(xtrain, ytrain, test_size=0.25, random_state=3)
    
    model = Earth()
    mars_model = model.fit(xtrain, ytrain)
    if request.method == 'POST':
    #General Details
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        current_year = request.POST.get('current_year')
        shs_strand = request.POST.get('shs_strand')
        first_choice = request.POST.get('first_choice')
        second_choice = request.POST.get('second_choice')
        third_choice = request.POST.get('third_choice')
        current_course = request.POST.get('current_course')
        current_college = request.POST.get('current_college')
        course_enviroment5 = request.POST.get('no_of_stud')
        
    #Decision Making Question
        decision_making1 = 1
        decision_making2 = 1
        decision_making3 = 1
        decision_making4 = 1
        if request.POST.get('dm1') == "1":
            decision_making1 = 4
        elif request.POST.get('dm1') == "2":
            decision_making1 = 3
        elif request.POST.get('dm1') == "3":
            decision_making1 = 2
        elif request.POST.get('dm1') == "4":
            decision_making1 = 1
        if request.POST.get('dm2') == "1":
            decision_making2 = 4
        elif request.POST.get('dm2') == "2":
            decision_making2 = 3
        elif request.POST.get('dm2') == "3":
            decision_making2 = 2
        elif request.POST.get('dm2') == "4":
            decision_making2 = 1
        if request.POST.get('dm3') == "1":
            decision_making3 = 4
        elif request.POST.get('dm3') == "2":
            decision_making3 = 3
        elif request.POST.get('dm3') == "3":
            decision_making3 = 2
        elif request.POST.get('dm3') == "4":
            decision_making3 = 1
        if request.POST.get('dm4') == "1":
            decision_making4 = 4
        elif request.POST.get('dm4') == "2":
            decision_making4 = 3
        elif request.POST.get('dm4') == "3":
            decision_making4 = 2
        elif request.POST.get('dm4') == "4":
            decision_making4 = 1
        decision_making5 = request.POST.get('decision_making5')

    #Personal Assessment Question
        personal_assessment1 = 1
        personal_assessment2 = 1
        personal_assessment3 = 1
        personal_assessment5 = 1
        if request.POST.get('pa1') == "1":
            personal_assessment1 = 4
        elif request.POST.get('pa1') == "2":
            personal_assessment1 = 3
        elif request.POST.get('pa1') == "3":
            personal_assessment1 = 2
        elif request.POST.get('pa1') == "4":
            personal_assessment1 = 1
        if request.POST.get('pa2') == "1":
            personal_assessment2 = 4
        elif request.POST.get('pa2') == "2":
            personal_assessment2 = 3
        elif request.POST.get('pa2') == "3":
            personal_assessment2 = 2
        elif request.POST.get('pa2') == "4":
            personal_assessment2 = 1
        if request.POST.get('pa3') == "1":
            personal_assessment3 = 4
        elif request.POST.get('pa3') == "2":
            personal_assessment3 = 3
        elif request.POST.get('pa3') == "3":
            personal_assessment3 = 2
        elif request.POST.get('pa3') == "4":
            personal_assessment3 = 1
        if request.POST.get('pa5') == "1":
            personal_assessment5 = 4
        elif request.POST.get('pa5') == "2":
            personal_assessment5 = 3
        elif request.POST.get('pa5') == "3":
            personal_assessment5 = 2
        elif request.POST.get('pa5') == "4":
            personal_assessment5 = 1
        personal_assessment4 = request.POST.get('personal_assesment4')
    #Course Enviroment Question
        course_enviroment1 = 1
        course_enviroment2 = 1
        course_enviroment3 = 1
        course_enviroment4 = 1
        if request.POST.get('ce1') == "1":
            course_enviroment1 = 4
        elif request.POST.get('ce1') == "2":
            course_enviroment1 = 3
        elif request.POST.get('ce1') == "3":
            course_enviroment1 = 2
        elif request.POST.get('ce1') == "4":
            course_enviroment1 = 1
        if request.POST.get('ce2') == "1":
            course_enviroment2 = 4
        elif request.POST.get('ce2') == "2":
            course_enviroment2 = 3
        elif request.POST.get('ce2') == "3":
            course_enviroment2 = 2
        elif request.POST.get('ce2') == "4":
            course_enviroment2 = 1
        if request.POST.get('ce3') == "1":
            course_enviroment3 = 4
        elif request.POST.get('ce3') == "2":
            course_enviroment3 = 3
        elif request.POST.get('ce3') == "3":
            course_enviroment3 = 2
        elif request.POST.get('ce3') == "4":
            course_enviroment3 = 1
        if request.POST.get('ce4') == "1":
            course_enviroment4 = 4
        elif request.POST.get('ce4') == "2":
            course_enviroment4 = 3
        elif request.POST.get('ce4') == "3":
            course_enviroment4 = 2
        elif request.POST.get('ce4') == "4":
            course_enviroment4 = 1
    #Course Satisfaction Question
        course_satisfaction1 = 1
        course_satisfaction2 = 1
        course_satisfaction3 = 1
        course_satisfaction4 = 1
        course_satisfaction5 = 1
        if request.POST.get('cs1') == "1":
            course_satisfaction1 = 4
        elif request.POST.get('cs1') == "2":
            course_satisfaction1 = 3
        elif request.POST.get('cs1') == "3":
            course_satisfaction1 = 2
        elif request.POST.get('cs1') == "4":
            course_satisfaction1 = 1
        if request.POST.get('cs2') == "1":
            course_satisfaction2 = 4
        elif request.POST.get('cs2') == "2":
            course_satisfaction2 = 3
        elif request.POST.get('cs2') == "3":
            course_satisfaction2 = 2
        elif request.POST.get('cs2') == "4":
            course_satisfaction2 = 1
        if request.POST.get('cs3') == "1":
            course_satisfaction3 = 4
        elif request.POST.get('cs3') == "2":
            course_satisfaction3 = 3
        elif request.POST.get('cs3') == "3":
            course_satisfaction3 = 2
        elif request.POST.get('cs3') == "4":
            course_satisfaction3 = 1
        if request.POST.get('cs4') == "1":
            course_satisfaction4 = 4
        elif request.POST.get('cs4') == "2":
            course_satisfaction4 = 3
        elif request.POST.get('cs4') == "3":
            course_satisfaction4 = 2
        elif request.POST.get('cs4') == "4":
            course_satisfaction4 = 1
        if request.POST.get('cs5') == "1":
            course_satisfaction5 = 4
        elif request.POST.get('cs5') == "2":
            course_satisfaction5 = 3
        elif request.POST.get('cs5') == "3":
            course_satisfaction5 = 2
        elif request.POST.get('cs5') == "4":
            course_satisfaction5 = 1
    #Academic Experience
        academic_experience1 = 1
        academic_experience2 = 1
        academic_experience3 = 1
        academic_experience4 = 1
        academic_experience5 = 1
        if request.POST.get('ae1') == "1":
            academic_experience1 = 4
        elif request.POST.get('ae1') == "2":
            academic_experience1 = 3
        elif request.POST.get('ae1') == "3":
            academic_experience1 = 2
        elif request.POST.get('ae1') == "4":
            academic_experience1 = 1
        if request.POST.get('ae2') == "1":
            academic_experience2 = 4
        elif request.POST.get('ae2') == "2":
            academic_experience2 = 3
        elif request.POST.get('ae2') == "3":
            academic_experience2 = 2
        elif request.POST.get('ae2') == "4":
            academic_experience2 = 1
        if request.POST.get('ae3') == "1":
            academic_experience3 = 4
        elif request.POST.get('ae3') == "2":
            academic_experience3 = 3
        elif request.POST.get('ae3') == "3":
            academic_experience3 = 2
        elif request.POST.get('ae3') == "4":
            academic_experience3 = 1
        if request.POST.get('ae4') == "1":
            academic_experience4 = 4
        elif request.POST.get('ae4') == "2":
            academic_experience4 = 3
        elif request.POST.get('ae4') == "3":
            academic_experience4 = 2
        elif request.POST.get('ae4') == "4":
            academic_experience4 = 1
        if request.POST.get('ae5') == "1":
            academic_experience5 = 4
        elif request.POST.get('ae5') == "2":
            academic_experience5 = 3
        elif request.POST.get('ae5') == "3":
            academic_experience5 = 2
        elif request.POST.get('ae5') == "4":
            academic_experience5 = 1
        
        
        #Prediction
     
        a = [[decision_making1,decision_making2,decision_making3,decision_making4,decision_making5,personal_assessment1,personal_assessment2,personal_assessment3,personal_assessment4,personal_assessment5,course_enviroment1,course_enviroment2,course_enviroment3,course_enviroment4,course_enviroment5,course_satisfaction1,course_satisfaction2,course_satisfaction3,course_satisfaction4,course_satisfaction5,academic_experience1,academic_experience2,academic_experience3,academic_experience4,academic_experience5]]
  
        # model = Earth()
        # MARS = model.fit(X_train, y_train)
    
        predict1 = mars_model.predict(a) > 0.43
        #pred = predict1*100
        context.update({'predict1':predict1})
        if predict1 == 1:
            shiftDecision = 1
        else:
            shiftDecision = 0
        create = Student(first_name=first_name,last_name=last_name,gender=gender,current_year=current_year,current_college=current_college,shs_strand=shs_strand,first_choice=first_choice,second_choice=second_choice,third_choice=third_choice,current_course=current_course,decision_making1=decision_making1,decision_making2=decision_making2,decision_making3=decision_making3,decision_making4=decision_making4,decision_making5=decision_making5,personal_assessment1=personal_assessment1,personal_assessment2=personal_assessment2,personal_assessment3=personal_assessment3,personal_assessment4=personal_assessment4,personal_assessment5=personal_assessment5,course_enviroment1=course_enviroment1,course_enviroment2=course_enviroment2,course_enviroment3=course_enviroment3,course_enviroment4=course_enviroment4,course_enviroment5=course_enviroment5,course_satisfaction1=course_satisfaction1,course_satisfaction2=course_satisfaction2,course_satisfaction3=course_satisfaction3,course_satisfaction4=course_satisfaction4,course_satisfaction5=course_satisfaction5,academic_experience1=academic_experience1,academic_experience2=academic_experience2,academic_experience3=academic_experience3,academic_experience4=academic_experience4,academic_experience5=academic_experience5,result=predict1,shiftDecision=shiftDecision)
        create.save()
        request.session['id'] = create.id 
        request.session['result'] = int(predict1[0])
        return redirect('test_result') 
    

    return render(request, 'test.html', context)

def signin(request):
    context = {
        'page':'login'
    }
    if request.method == 'POST':
        username = request.POST.get('InputEmail')
        password = request.POST.get('InputPassword')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_authenticated:
                return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect!')
            return redirect('login') 
    return render(request, 'login.html', context)
@login_required(login_url='login')
def signout(request):
    logout(request)
    messages.success(request, 'Your account has been logged out.')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    first_year = 0
    second_year = 0
    third_year = 0
    fourth_year = 0
    fifth_year = 0
    sixth_year = 0
    gender_male = 0
    gender_female = 0

    user = CustomUser.objects.all()
    student = Student.objects.all()
    cet = Student.objects.filter(current_college='CET')
    plmbs = Student.objects.filter(current_college='PLMBS')
    first_year = Student.objects.filter(current_year=1)
    second_year = Student.objects.filter(current_year=2)
    third_year = Student.objects.filter(current_year=3)
    fourth_year = Student.objects.filter(current_year=4)
    fifth_year = Student.objects.filter(current_year=5)
    sixth_year = Student.objects.filter(current_year=6)
    gender_male = Student.objects.filter(gender='Male')
    gender_female = Student.objects.filter(gender='Female')
    current_datetime = datetime.date.today()

    
    cetGenderM = 0
    cetGenderF = 0
    cetFirstYr = 0
    cetSecondYr = 0
    cetThirdYr = 0
    cetFourthYr = 0
    cetFifthYr = 0
    cetSixthYr = 0
    plmbsGenderM = 0
    plmbsGenderF = 0
    plmbsFirstYr = 0
    plmbsSecondYr = 0
    plmbsThirdYr = 0
    plmbsFourthYr = 0
    plmbsFifthYr = 0
    plmbsSixthYr = 0

    #genderCET
    cetGenderM = Student.objects.filter(current_college='CET').filter(gender='Male').count
    cetGenderF = Student.objects.filter(current_college='CET').filter(gender='Female').count
    #StudentYrCET
    cetFirstYr = Student.objects.filter(current_year=1).filter(current_college='CET').count
    cetSecondYr = Student.objects.filter(current_year=2).filter(current_college='CET').count
    cetThirdYr = Student.objects.filter(current_year=3).filter(current_college='CET').count
    cetFourthYr = Student.objects.filter(current_year=4).filter(current_college='CET').count
    cetFifthYr = Student.objects.filter(current_year=5).filter(current_college='CET').count
    cetSixthYr = Student.objects.filter(current_year=6).filter(current_college='CET').count
    #genderPLMBS
    plmbsGenderM = Student.objects.filter(current_college='PLMBS').filter(gender='Male').count
    plmbsGenderF = Student.objects.filter(current_college='PLMBS').filter(gender='Female').count
    #StudentYrPLMBS
    plmbsFirstYr = Student.objects.filter(current_year=1).filter(current_college='PLMBS').count
    plmbsSecondYr = Student.objects.filter(current_year=2).filter(current_college='PLMBS').count
    plmbsThirdYr = Student.objects.filter(current_year=3).filter(current_college='PLMBS').count
    plmbsFourthYr = Student.objects.filter(current_year=4).filter(current_college='PLMBS').count
    plmbsFifthYr = Student.objects.filter(current_year=5).filter(current_college='PLMBS').count
    plmbsSixthYr = Student.objects.filter(current_year=6).filter(current_college='PLMBS').count
    
    #First Year CET
    bsitShift1 = 0
    bsitStay1 = 0
    bscsShift1 = 0
    bscsStay1 = 0
    bscheShift1 = 0
    bscheStay1 = 0
    bsceShift1 = 0
    bsceStay1 = 0
    bscpeShift1 = 0
    bscpeStay1 = 0
    bseeShift1 = 0
    bseeStay1 = 0
    bseceShift1 = 0
    bseceStay1 = 0
    bsmeShift1 = 0
    bsmeStay1 = 0
    bsmfgeShift1 = 0
    bsmfgeStay1 = 0
    #First Year PLMBS
    bsaShift1 = 0
    bsaStay1 = 0
    bsbafmShift1 = 0
    bsbafmStay1 = 0
    bsbammShift1 = 0
    bsbammStay1 = 0
    bsbaomShift1 = 0
    bsbaomStay1 = 0
    bsbahrmShift1 = 0
    bsbahrmStay1 = 0
    bsbabeShift1 = 0
    bsbabeStay1 = 0
    bsentreShift1 = 0
    bsentreStay1 = 0
    bsremShift1 = 0
    bsremStay1 = 0
    bshmShift1 = 0
    bshmStay1 = 0
    bstmShift1 = 0
    bstmStay1 = 0

    #Chairperson stats per year
    #FIrst Year
    for n in first_year:
        #CET
        if n.current_course=='BS Information and Technology':
            if n.result == 1:
                bsitShift1+=1
            else:
                bsitStay1+=1
        if n.current_course=='BS Computer Science':
            if n.result == 1:
                bscsShift1+=1
            else:
                bscsStay1+=1
        elif n.current_course == 'BS Chemical Engineering (BSCHE)':
            if n.result == 1:
                bscheShift1+=1
            else:
                bscheStay1+=1
        elif n.current_course == 'BS Civil Engineering (BSCE)':
            if n.result == 1:
                bsceShift1+=1
            else:
                bsceStay1+=1
        elif n.current_course == 'BS Computer Engineering (BSCpE)':
            if n.result == 1:
                bscpeShift1+=1
            else:
                bscpeStay1+=1
        elif n.current_course == 'BS Electrical Engineering (BSEE)':
            if n.result == 1:
                bseeShift1+=1
            else:
                bseeStay1+=1
        elif n.current_course == 'BS Electronics Engineering (BSECE)':
            if n.result == 1:
                bseceShift1+=1
            else:
                bseceStay1+=1
        elif n.current_course == 'BS Mechanical Engineering (BSME)':
            if n.result == 1:
                bsmeShift1+=1
            else:
                bsmeStay1+=1
        elif n.current_course == 'BS Manufacturing Engineering (BSMfgE)':
            if n.result == 1:
                bsmfgeShift1+=1
            else:
                bsmfgeStay1+=1
    #PLMBS
        elif n.current_course == 'Bachelor of Science in Accountancy (BSA)':
            if n.result == 1:
                bsaShift1+=1
            else:
                bsaStay1+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)':
            if n.result == 1:
                bsbafmShift1+=1
            else:
                bsbafmStay1+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)':
            if n.result == 1:
                bsbammShift1+=1
            else:
                bsbammStay1+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)':
            if n.result == 1:
                bsbaomShift1+=1
            else:
                bsbaomStay1+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)':
            if n.result == 1:
                bsbahrmShift1+=1
            else:
                bsbahrmStay1+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)':
            if n.result == 1:
                bsbabeShift1+=1
            else:
                bsbabeStay1+=1
        elif n.current_course == 'Bachelor of Science in Entrepreneurship (BS ENTRE)':
            if n.result == 1:
                bsentreShift1+=1
            else:
                bsentreStay1+=1
        elif n.current_course == 'Bachelor of Science in Real Estate Management (BSREM)':
            if n.result == 1:
                bsremShift1+=1
            else:
                bsremStay1+=1        
        elif n.current_course == 'Bachelor of Science in Hospitality Management (BSHM)':
            if n.result == 1:
                bshmShift1+=1
            else:
                bshmStay1+=1   
        elif n.current_course == 'Bachelor of Science in Tourism Management (BSTM)':
            if n.result == 1:
                bstmShift1+=1
            else:
                bstmStay1+=1 
    
    #Second Year CET
    bsitShift2 = 0
    bsitStay2 = 0
    bscsShift2 = 0
    bscsStay2 = 0
    bscheShift2 = 0
    bscheStay2 = 0
    bsceShift2 = 0
    bsceStay2 = 0
    bscpeShift2 = 0
    bscpeStay2 = 0
    bseeShift2 = 0
    bseeStay2 = 0
    bseceShift2 = 0
    bseceStay2 = 0
    bsmeShift2 = 0
    bsmeStay2 = 0
    bsmfgeShift2 = 0
    bsmfgeStay2 = 0
    #Second Year PLMBS
    bsaShift2 = 0
    bsaStay2 = 0
    bsbafmShift2 = 0
    bsbafmStay2 = 0
    bsbammShift2 = 0
    bsbammStay2 = 0
    bsbaomShift2 = 0
    bsbaomStay2 = 0
    bsbahrmShift2 = 0
    bsbahrmStay2 = 0
    bsbabeShift2 = 0
    bsbabeStay2 = 0
    bsentreShift2 = 0
    bsentreStay2 = 0
    bsremShift2 = 0
    bsremStay2 = 0
    bshmShift2 = 0
    bshmStay2 = 0
    bstmShift2 = 0
    bstmStay2 = 0

    #Second Year
    for n in second_year:
        #CET
        if n.current_course=='BS Information and Technology':
            if n.result == 1:
                bsitShift2+=1
            else:
                bsitStay2+=1
        elif n.current_course=='BS Computer Science':
            if n.result == 1:
                bscsShift2+=1
            else:
                bscsStay2+=1
        elif n.current_course == 'BS Chemical Engineering (BSCHE)':
            if n.result == 1:
                bscheShift2+=1
            else:
                bscheStay2+=1
        elif n.current_course == 'BS Civil Engineering (BSCE)':
            if n.result == 1:
                bsceShift2+=1
            else:
                bsceStay2+=1
        elif n.current_course == 'BS Computer Engineering (BSCpE)':
            if n.result == 1:
                bscpeShift2+=1
            else:
                bscpeStay2+=1
        elif n.current_course == 'BS Electrical Engineering (BSEE)':
            if n.result == 1:
                bseeShift2+=1
            else:
                bseeStay2+=1
        elif n.current_course == 'BS Electronics Engineering (BSECE)':
            if n.result == 1:
                bseceShift2+=1
            else:
                bseceStay2+=1
        elif n.current_course == 'BS Mechanical Engineering (BSME)':
            if n.result == 1:
                bsmeShift2+=1
            else:
                bsmeStay2+=1
        elif n.current_course == 'BS Manufacturing Engineering (BSMfgE)':
            if n.result == 1:
                bsmfgeShift2+=1
            else:
                bsmfgeStay2+=1
    #PLMBS
        elif n.current_course == 'Bachelor of Science in Accountancy (BSA)':
            if n.result == 1:
                bsaShift2+=1
            else:
                bsaStay2+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)':
            if n.result == 1:
                bsbafmShift2+=1
            else:
                bsbafmStay2+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)':
            if n.result == 1:
                bsbammShift2+=1
            else:
                bsbammStay2+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)':
            if n.result == 1:
                bsbaomShift2+=1
            else:
                bsbaomStay2+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)':
            if n.result == 1:
                bsbahrmShift2+=1
            else:
                bsbahrmStay2+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)':
            if n.result == 1:
                bsbabeShift2+=1
            else:
                bsbabeStay2+=1
        elif n.current_course == 'Bachelor of Science in Entrepreneurship (BS ENTRE)':
            if n.result == 1:
                bsentreShift2+=1
            else:
                bsentreStay2+=1
        elif n.current_course == 'Bachelor of Science in Real Estate Management (BSREM)':
            if n.result == 1:
                bsremShift2+=1
            else:
                bsremStay2+=1        
        elif n.current_course == 'Bachelor of Science in Hospitality Management (BSHM)':
            if n.result == 1:
                bshmShift2+=1
            else:
                bshmStay2+=1   
        elif n.current_course == 'Bachelor of Science in Tourism Management (BSTM)':
            if n.result == 1:
                bstmShift2+=1
            else:
                bstmStay2+=1 

    #Third Year CET
    bsitShift3 = 0
    bsitStay3 = 0
    bscsShift3 = 0
    bscsStay3 = 0
    bscheShift3 = 0
    bscheStay3 = 0
    bsceShift3 = 0
    bsceStay3 = 0
    bscpeShift3 = 0
    bscpeStay3 = 0
    bseeShift3 = 0
    bseeStay3 = 0
    bseceShift3 = 0
    bseceStay3 = 0
    bsmeShift3 = 0
    bsmeStay3 = 0
    bsmfgeShift3 = 0
    bsmfgeStay3 = 0
    #Third Year PLMBS
    bsaShift3 = 0
    bsaStay3 = 0
    bsbafmShift3 = 0
    bsbafmStay3 = 0
    bsbammShift3 = 0
    bsbammStay3 = 0
    bsbaomShift3 = 0
    bsbaomStay3 = 0
    bsbahrmShift3 = 0
    bsbahrmStay3 = 0
    bsbabeShift3 = 0
    bsbabeStay3 = 0
    bsentreShift3 = 0
    bsentreStay3 = 0
    bsremShift3 = 0
    bsremStay3 = 0
    bshmShift3 = 0
    bshmStay3 = 0
    bstmShift3 = 0
    bstmStay3 = 0

    #Third Year
    for n in third_year:
        #CET
        if n.current_course=='BS Information and Technology':
            if n.result == 1:
                bsitShift3+=1
            else:
                bsitStay3+=1
        elif n.current_course=='BS Computer Science':
            if n.result == 1:
                bscsShift3+=1
            else:
                bscsStay3+=1
        elif n.current_course == 'BS Chemical Engineering (BSCHE)':
            if n.result == 1:
                bscheShift3+=1
            else:
                bscheStay3+=1
        elif n.current_course == 'BS Civil Engineering (BSCE)':
            if n.result == 1:
                bsceShift3+=1
            else:
                bsceStay3+=1
        elif n.current_course == 'BS Computer Engineering (BSCpE)':
            if n.result == 1:
                bscpeShift3+=1
            else:
                bscpeStay3+=1
        elif n.current_course == 'BS Electrical Engineering (BSEE)':
            if n.result == 1:
                bseeShift3+=1
            else:
                bseeStay3+=1
        elif n.current_course == 'BS Electronics Engineering (BSECE)':
            if n.result == 1:
                bseceShift3+=1
            else:
                bseceStay3+=1
        elif n.current_course == 'BS Mechanical Engineering (BSME)':
            if n.result == 1:
                bsmeShift3+=1
            else:
                bsmeStay3+=1
        elif n.current_course == 'BS Manufacturing Engineering (BSMfgE)':
            if n.result == 1:
                bsmfgeShift3+=1
            else:
                bsmfgeStay3+=1
    #PLMBS
        elif n.current_course == 'Bachelor of Science in Accountancy (BSA)':
            if n.result == 1:
                bsaShift3+=1
            else:
                bsaStay3+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)':
            if n.result == 1:
                bsbafmShift3+=1
            else:
                bsbafmStay3+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)':
            if n.result == 1:
                bsbammShift3+=1
            else:
                bsbammStay3+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)':
            if n.result == 1:
                bsbaomShift3+=1
            else:
                bsbaomStay3+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)':
            if n.result == 1:
                bsbahrmShift3+=1
            else:
                bsbahrmStay3+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)':
            if n.result == 1:
                bsbabeShift3+=1
            else:
                bsbabeStay3+=1
        elif n.current_course == 'Bachelor of Science in Entrepreneurship (BS ENTRE)':
            if n.result == 1:
                bsentreShift3+=1
            else:
                bsentreStay3+=1
        elif n.current_course == 'Bachelor of Science in Real Estate Management (BSREM)':
            if n.result == 1:
                bsremShift3+=1
            else:
                bsremStay3+=1        
        elif n.current_course == 'Bachelor of Science in Hospitality Management (BSHM)':
            if n.result == 1:
                bshmShift3+=1
            else:
                bshmStay3+=1   
        elif n.current_course == 'Bachelor of Science in Tourism Management (BSTM)':
            if n.result == 1:
                bstmShift3+=1
            else:
                bstmStay3+=1 
    
    #Fourth Year CET
    bsitShift4 = 0
    bsitStay4 = 0
    bscsShift4 = 0
    bscsStay4 = 0
    bscheShift4 = 0
    bscheStay4 = 0
    bsceShift4 = 0
    bsceStay4 = 0
    bscpeShift4 = 0
    bscpeStay4 = 0
    bseeShift4 = 0
    bseeStay4 = 0
    bseceShift4 = 0
    bseceStay4 = 0
    bsmeShift4 = 0
    bsmeStay4 = 0
    bsmfgeShift4 = 0
    bsmfgeStay4 = 0
    #Fourth Year PLMBS
    bsaShift4 = 0
    bsaStay4 = 0
    bsbafmShift4 = 0
    bsbafmStay4 = 0
    bsbammShift4 = 0
    bsbammStay4 = 0
    bsbaomShift4 = 0
    bsbaomStay4 = 0
    bsbahrmShift4 = 0
    bsbahrmStay4 = 0
    bsbabeShift4 = 0
    bsbabeStay4 = 0
    bsentreShift4 = 0
    bsentreStay4 = 0
    bsremShift4 = 0
    bsremStay4 = 0
    bshmShift4 = 0
    bshmStay4 = 0
    bstmShift4 = 0
    bstmStay4 = 0

    #Fourth Year
    for n in fourth_year:
        #CET
        if n.current_course=='BS Information and Technology':
            if n.result == 1:
                bsitShift4+=1
            else:
                bsitStay4+=1
        elif n.current_course=='BS Computer Science':
            if n.result == 1:
                bscsShift4+=1
            else:
                bscsStay4+=1
        elif n.current_course == 'BS Chemical Engineering (BSCHE)':
            if n.result == 1:
                bscheShift4+=1
            else:
                bscheStay4+=1
        elif n.current_course == 'BS Civil Engineering (BSCE)':
            if n.result == 1:
                bsceShift4+=1
            else:
                bsceStay4+=1
        elif n.current_course == 'BS Computer Engineering (BSCpE)':
            if n.result == 1:
                bscpeShift4+=1
            else:
                bscpeStay4+=1
        elif n.current_course == 'BS Electrical Engineering (BSEE)':
            if n.result == 1:
                bseeShift4+=1
            else:
                bseeStay4+=1
        elif n.current_course == 'BS Electronics Engineering (BSECE)':
            if n.result == 1:
                bseceShift4+=1
            else:
                bseceStay4+=1
        elif n.current_course == 'BS Mechanical Engineering (BSME)':
            if n.result == 1:
                bsmeShift4+=1
            else:
                bsmeStay4+=1
        elif n.current_course == 'BS Manufacturing Engineering (BSMfgE)':
            if n.result == 1:
                bsmfgeShift4+=1
            else:
                bsmfgeStay4+=1
    #PLMBS
        elif n.current_course == 'Bachelor of Science in Accountancy (BSA)':
            if n.result == 1:
                bsaShift4+=1
            else:
                bsaStay4+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)':
            if n.result == 1:
                bsbafmShift4+=1
            else:
                bsbafmStay4+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)':
            if n.result == 1:
                bsbammShift4+=1
            else:
                bsbammStay4+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)':
            if n.result == 1:
                bsbaomShift4+=1
            else:
                bsbaomStay4+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)':
            if n.result == 1:
                bsbahrmShift4+=1
            else:
                bsbahrmStay4+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)':
            if n.result == 1:
                bsbabeShift4+=1
            else:
                bsbabeStay4+=1
        elif n.current_course == 'Bachelor of Science in Entrepreneurship (BS ENTRE)':
            if n.result == 1:
                bsentreShift4+=1
            else:
                bsentreStay4+=1
        elif n.current_course == 'Bachelor of Science in Real Estate Management (BSREM)':
            if n.result == 1:
                bsremShift4+=1
            else:
                bsremStay4+=1        
        elif n.current_course == 'Bachelor of Science in Hospitality Management (BSHM)':
            if n.result == 1:
                bshmShift4+=1
            else:
                bshmStay4+=1   
        elif n.current_course == 'Bachelor of Science in Tourism Management (BSTM)':
            if n.result == 1:
                bstmShift4+=1
            else:
                bstmStay4+=1

    #Fifth Year CET
    bsitShift5 = 0
    bsitStay5 = 0
    bscsShift5 = 0
    bscsStay5 = 0
    bscheShift5 = 0
    bscheStay5 = 0
    bsceShift5 = 0
    bsceStay5 = 0
    bscpeShift5 = 0
    bscpeStay5 = 0
    bseeShift5 = 0
    bseeStay5 = 0
    bseceShift5 = 0
    bseceStay5 = 0
    bsmeShift5 = 0
    bsmeStay5 = 0
    bsmfgeShift5 = 0
    bsmfgeStay5 = 0
    #Fifth Year PLMBS
    bsaShift5 = 0
    bsaStay5 = 0
    bsbafmShift5 = 0
    bsbafmStay5 = 0
    bsbammShift5 = 0
    bsbammStay5 = 0
    bsbaomShift5 = 0
    bsbaomStay5 = 0
    bsbahrmShift5 = 0
    bsbahrmStay5 = 0
    bsbabeShift5 = 0
    bsbabeStay5 = 0
    bsentreShift5 = 0
    bsentreStay5 = 0
    bsremShift5 = 0
    bsremStay5 = 0
    bshmShift5 = 0
    bshmStay5 = 0
    bstmShift5 = 0
    bstmStay5 = 0

    #Fifth Year
    for n in fifth_year:
        #CET
        if n.current_course=='BS Information and Technology':
            if n.result == 1:
                bsitShift5+=1
            else:
                bsitStay5+=1
        elif n.current_course=='BS Computer Science':
            if n.result == 1:
                bscsShift5+=1
            else:
                bscsStay5+=1
        elif n.current_course == 'BS Chemical Engineering (BSCHE)':
            if n.result == 1:
                bscheShift5+=1
            else:
                bscheStay5+=1
        elif n.current_course == 'BS Civil Engineering (BSCE)':
            if n.result == 1:
                bsceShift5+=1
            else:
                bsceStay5+=1
        elif n.current_course == 'BS Computer Engineering (BSCpE)':
            if n.result == 1:
                bscpeShift5+=1
            else:
                bscpeStay5+=1
        elif n.current_course == 'BS Electrical Engineering (BSEE)':
            if n.result == 1:
                bseeShift5+=1
            else:
                bseeStay5+=1
        elif n.current_course == 'BS Electronics Engineering (BSECE)':
            if n.result == 1:
                bseceShift5+=1
            else:
                bseceStay5+=1
        elif n.current_course == 'BS Mechanical Engineering (BSME)':
            if n.result == 1:
                bsmeShift5+=1
            else:
                bsmeStay5+=1
        elif n.current_course == 'BS Manufacturing Engineering (BSMfgE)':
            if n.result == 1:
                bsmfgeShift5+=1
            else:
                bsmfgeStay5+=1
    #PLMBS
        elif n.current_course == 'Bachelor of Science in Accountancy (BSA)':
            if n.result == 1:
                bsaShift5+=1
            else:
                bsaStay5+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)':
            if n.result == 1:
                bsbafmShift5+=1
            else:
                bsbafmStay5+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)':
            if n.result == 1:
                bsbammShift5+=1
            else:
                bsbammStay5+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)':
            if n.result == 1:
                bsbaomShift5+=1
            else:
                bsbaomStay5+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)':
            if n.result == 1:
                bsbahrmShift5+=1
            else:
                bsbahrmStay5+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)':
            if n.result == 1:
                bsbabeShift5+=1
            else:
                bsbabeStay5+=1
        elif n.current_course == 'Bachelor of Science in Entrepreneurship (BS ENTRE)':
            if n.result == 1:
                bsentreShift5+=1
            else:
                bsentreStay5+=1
        elif n.current_course == 'Bachelor of Science in Real Estate Management (BSREM)':
            if n.result == 1:
                bsremShift5+=1
            else:
                bsremStay5+=1        
        elif n.current_course == 'Bachelor of Science in Hospitality Management (BSHM)':
            if n.result == 1:
                bshmShift5+=1
            else:
                bshmStay5+=1   
        elif n.current_course == 'Bachelor of Science in Tourism Management (BSTM)':
            if n.result == 1:
                bstmShift5+=1
            else:
                bstmStay5+=1  

    #Sixth Year CET
    bsitShift6 = 0
    bsitStay6 = 0
    bscsShift6 = 0
    bscsStay6 = 0
    bscheShift6 = 0
    bscheStay6 = 0
    bsceShift6 = 0
    bsceStay6 = 0
    bscpeShift6 = 0
    bscpeStay6 = 0
    bseeShift6 = 0
    bseeStay6 = 0
    bseceShift6 = 0
    bseceStay6 = 0
    bsmeShift6 = 0
    bsmeStay6 = 0
    bsmfgeShift6 = 0
    bsmfgeStay6 = 0
    #Sixth Year PLMBS
    bsaShift6 = 0
    bsaStay6 = 0
    bsbafmShift6 = 0
    bsbafmStay6 = 0
    bsbammShift6 = 0
    bsbammStay6 = 0
    bsbaomShift6 = 0
    bsbaomStay6 = 0
    bsbahrmShift6 = 0
    bsbahrmStay6 = 0
    bsbabeShift6 = 0
    bsbabeStay6 = 0
    bsentreShift6 = 0
    bsentreStay6 = 0
    bsremShift6 = 0
    bsremStay6 = 0
    bshmShift6 = 0
    bshmStay6 = 0
    bstmShift6 = 0
    bstmStay6 = 0

    #Sixth Year
    for n in sixth_year:
        #CET
        if n.current_course=='BS Information and Technology':
            if n.result == 1:
                bsitShift6+=1
            else:
                bsitStay6+=1
        elif n.current_course=='BS Computer Science':
            if n.result == 1:
                bscsShift6+=1
            else:
                bscsStay6+=1
        elif n.current_course == 'BS Chemical Engineering (BSCHE)':
            if n.result == 1:
                bscheShift6+=1
            else:
                bscheStay6+=1
        elif n.current_course == 'BS Civil Engineering (BSCE)':
            if n.result == 1:
                bsceShift6+=1
            else:
                bsceStay6+=1
        elif n.current_course == 'BS Computer Engineering (BSCpE)':
            if n.result == 1:
                bscpeShift6+=1
            else:
                bscpeStay6+=1
        elif n.current_course == 'BS Electrical Engineering (BSEE)':
            if n.result == 1:
                bseeShift6+=1
            else:
                bseeStay6+=1
        elif n.current_course == 'BS Electronics Engineering (BSECE)':
            if n.result == 1:
                bseceShift6+=1
            else:
                bseceStay6+=1
        elif n.current_course == 'BS Mechanical Engineering (BSME)':
            if n.result == 1:
                bsmeShift6+=1
            else:
                bsmeStay6+=1
        elif n.current_course == 'BS Manufacturing Engineering (BSMfgE)':
            if n.result == 1:
                bsmfgeShift6+=1
            else:
                bsmfgeStay6+=1
    #PLMBS
        elif n.current_course == 'Bachelor of Science in Accountancy (BSA)':
            if n.result == 1:
                bsaShift6+=1
            else:
                bsaStay6+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)':
            if n.result == 1:
                bsbafmShift6+=1
            else:
                bsbafmStay6+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)':
            if n.result == 1:
                bsbammShift6+=1
            else:
                bsbammStay6+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)':
            if n.result == 1:
                bsbaomShift6+=1
            else:
                bsbaomStay6+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)':
            if n.result == 1:
                bsbahrmShift6+=1
            else:
                bsbahrmStay6+=1
        elif n.current_course == 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)':
            if n.result == 1:
                bsbabeShift6+=1
            else:
                bsbabeStay6+=1
        elif n.current_course == 'Bachelor of Science in Entrepreneurship (BS ENTRE)':
            if n.result == 1:
                bsentreShift6+=1
            else:
                bsentreStay6+=1
        elif n.current_course == 'Bachelor of Science in Real Estate Management (BSREM)':
            if n.result == 1:
                bsremShift6+=1
            else:
                bsremStay6+=1        
        elif n.current_course == 'Bachelor of Science in Hospitality Management (BSHM)':
            if n.result == 1:
                bshmShift6+=1
            else:
                bshmStay6+=1   
        elif n.current_course == 'Bachelor of Science in Tourism Management (BSTM)':
            if n.result == 1:
                bstmShift6+=1
            else:
                bstmStay6+=1  

#Chairperson Stats
#CET
    #BSIT
    bsitShift = bsitShift1+bsitShift2+bsitShift3+bsitShift4+bsitShift5+bsitShift6
    bsitStay = bsitStay1+bsitStay2+bsitStay3+bsitStay4+bsitStay5+bsitStay6
    #BSCS
    bscsShift = bscsShift1+bscsShift2+bscsShift3+bscsShift4+bscsShift5+bscsShift6
    bscsStay = bscsStay1+bscsStay2+bscsStay3+bscsStay4+bscsStay5+bscsStay6
    #BSCHE
    bscheShift = bscheShift1+bscheShift2+bscheShift3+bscheShift4+bscheShift5+bscheShift6
    bscheStay = bscheStay1+bscheStay2+bscheStay3+bscheStay4+bscheStay5+bscheStay6
    #BSCE
    bsceShift = bsceShift1+bsceShift2+bsceShift3+bsceShift4+bsceShift5+bsceShift6
    bsceStay = bsceStay1+bsceStay2+bsceStay3+bsceStay4+bsceStay5+bsceStay6
    #BSCPE
    bscpeShift = bscpeShift1+bscpeShift2+bscpeShift3+bscpeShift4+bscpeShift5+bscpeShift6
    bscpeStay = bscpeStay1+bscpeStay2+bscpeStay3+bscpeStay4+bscpeStay5+bscpeStay6
    #BSEE
    bseeShift = bseeShift1+bseeShift2+bseeShift3+bseeShift4+bseeShift5+bseeShift6
    bseeStay = bseeStay1+bseeStay2+bseeStay3+bseeStay4+bseeStay5+bseeStay6
    #BSECE
    bseceShift = bseceShift1+bseceShift2+bseceShift3+bseceShift4+bseceShift5+bseceShift6
    bseceStay = bseceStay1+bseceStay2+bseceStay3+bseceStay4+bseceStay5+bseceStay6
    #BSME
    bsmeShift = bsmeShift1+bsmeShift2+bsmeShift3+bsmeShift4+bsmeShift5+bsmeShift6
    bsmeStay = bsmeStay1+bsmeStay2+bsmeStay3+bsmeStay4+bsmeStay5+bsmeStay6
    #BSMfgE
    bsmfgeShift = bsmfgeShift1+bsmfgeShift2+bsmfgeShift3+bsmfgeShift4+bsmfgeShift5+bsmfgeShift6
    bsmfgeStay = bsmfgeStay1+bsmfgeStay2+bsmfgeStay3+bsmfgeStay4+bsmfgeStay5+bsmfgeStay6
    #1st Year CET
    cetshift1 = bsitShift1+bscsShift1+bscheShift1+bsceShift1+bscpeShift1+bseeShift1+bseceShift1+bsmeShift1+bsmfgeShift1
    cetstay1 = bsitStay1+bscsStay1+bscheStay1+bsceStay1+bscpeStay1+bseeStay1+bseceStay1+bsmeStay1+bsmfgeStay1
    #2nd Year CET
    cetshift2 = bsitShift2+bscsShift2+bscheShift2+bsceShift2+bscpeShift2+bseeShift2+bseceShift2+bsmeShift2+bsmfgeShift2
    cetstay2 = bsitStay2+bscsStay2+bscheStay2+bsceStay2+bscpeStay2+bseeStay2+bseceStay2+bsmeStay2+bsmfgeStay2
    #3rd Year CET
    cetshift3 = bsitShift3+bscsShift3+bscheShift3+bsceShift3+bscpeShift3+bseeShift3+bseceShift3+bsmeShift3+bsmfgeShift3
    cetstay3 = bsitStay3+bscsStay3+bscheStay3+bsceStay3+bscpeStay3+bseeStay3+bseceStay3+bsmeStay3+bsmfgeStay3
    #4th Year CET
    cetshift4 = bsitShift4+bscsShift4+bscheShift4+bsceShift4+bscpeShift4+bseeShift4+bseceShift4+bsmeShift4+bsmfgeShift4
    cetstay4 = bsitStay4+bscsStay4+bscheStay4+bsceStay4+bscpeStay4+bseeStay4+bseceStay4+bsmeStay4+bsmfgeStay4
    #5th Year CET
    cetshift5 = bsitShift5+bscsShift5+bscheShift5+bsceShift5+bscpeShift5+bseeShift5+bseceShift5+bsmeShift5+bsmfgeShift5
    cetstay5 = bsitStay5+bscsStay5+bscheStay5+bsceStay5+bscpeStay5+bseeStay5+bseceStay5+bsmeStay5+bsmfgeStay5
    #6th Year CET
    cetshift6 = bsitShift6+bscsShift6+bscheShift6+bsceShift6+bscpeShift6+bseeShift6+bseceShift6+bsmeShift6+bsmfgeShift6
    cetstay6 = bsitStay6+bscsStay6+bscheStay6+bsceStay6+bscpeStay6+bseeStay6+bseceStay6+bsmeStay6+bsmfgeStay6
    #Whole CET
    cetshift = bsitShift+bscsShift+bscheShift+bsceShift+bscpeShift+bseeShift+bseceShift+bsmeShift+bsmfgeShift
    cetstay = bsitStay+bscsStay+bscheStay+bsceShift+bscpeStay+bseeStay+bseceStay+bsmeStay+bsmfgeStay

#PLMBS
    #BSA
    bsaShift = bsaShift1+bsaShift2+bsaShift3+bsaShift4+bsaShift5+bsaShift6
    bsaStay = bsaStay1+bsaStay2+bsaStay3+bsaStay4+bsaStay5+bsaStay6
    #BSBA FM
    bsbafmShift = bsbafmShift1+bsbafmShift2+bsbafmShift3+bsbafmShift4+bsbafmShift5+bsbafmShift6
    bsbafmStay = bsbafmStay1+bsbafmStay2+bsbafmStay3+bsbafmStay4+bsbafmStay5+bsbafmStay6
    #BSBA MM
    bsbammShift = bsbammShift1+bsbammShift2+bsbammShift3+bsbammShift4+bsbammShift5+bsbammShift6
    bsbammStay = bsbammStay1+bsbammStay2+bsbammStay3+bsbammStay4+bsbammStay5+bsbammStay6
    #BSBA OM
    bsbaomShift = bsbaomShift1+bsbaomShift2+bsbaomShift3+bsbaomShift4+bsbaomShift5+bsbaomShift6
    bsbaomStay = bsbaomStay1+bsbaomStay2+bsbaomStay3+bsbaomStay4+bsbaomStay5+bsbaomStay6
    #BSBA HRM
    bsbahrmShift = bsbahrmShift1+bsbahrmShift2+bsbahrmShift3+bsbahrmShift4+bsbahrmShift5+bsbahrmShift6
    bsbahrmStay = bsbahrmStay1+bsbahrmStay2+bsbahrmStay3+bsbahrmStay4+bsbahrmStay5+bsbahrmStay6
    #BSBA BE
    bsbabeShift = bsbabeShift1+bsbabeShift2+bsbabeShift3+bsbabeShift4+bsbabeShift5+bsbabeShift6
    bsbabeStay = bsbabeStay1+bsbabeStay2+bsbabeStay3+bsbabeStay4+bsbabeStay5+bsbabeStay6
    #BSEntre
    bsentreShift = bsentreShift1+bsentreShift2+bsentreShift3+bsentreShift4+bsentreShift5+bsentreShift6
    bsentreStay = bsentreStay1+bsentreStay2+bsentreStay3+bsentreStay4+bsentreStay5+bsentreStay6
    #BSRem
    bsremShift = bsremShift1+bsremShift2+bsremShift3+bsremShift4+bsremShift5+bsremShift6
    bsremStay = bsremStay1+bsremStay2+bsremStay3+bsremStay4+bsremStay5+bsremStay6
    #BSHM
    bshmShift = bshmShift1+bshmShift2+bshmShift3+bshmShift4+bshmShift5+bshmShift6
    bshmStay = bshmStay1+bshmStay2+bshmStay3+bshmStay4+bshmStay5+bshmStay6
    #BSTM
    bstmShift = bstmShift1+bstmShift2+bstmShift3+bstmShift4+bstmShift5+bstmShift6
    bstmStay = bstmStay1+bstmStay2+bstmStay3+bstmStay4+bstmStay5+bstmStay6

    #1st Year PLMBS
    plmbsshift1 = bsaShift1+bsbafmShift1+bsbammShift1+bsbaomShift1+bsbahrmShift1+bsbabeShift1+bsentreShift1+bsremShift1+bshmShift1+bstmShift1
    plmbsstay1 = bsaStay1+bsbafmStay1+bsbammStay1+bsbaomStay1+bsbahrmStay1+bsbabeStay1+bsentreStay1+bsremStay1+bshmStay1+bstmStay1
    #2nd Year PLMBS
    plmbsshift2 = bsaShift2+bsbafmShift2+bsbammShift2+bsbaomShift2+bsbahrmShift2+bsbabeShift2+bsentreShift2+bsremShift2+bshmShift2+bstmShift2
    plmbsstay2 = bsaStay2+bsbafmStay2+bsbammStay2+bsbaomStay2+bsbahrmStay2+bsbabeStay2+bsentreStay2+bsremStay2+bshmStay2+bstmStay2
    #3rd Year PLMBS
    plmbsshift3 = bsaShift3+bsbafmShift3+bsbammShift3+bsbaomShift3+bsbahrmShift3+bsbabeShift3+bsentreShift3+bsremShift3+bshmShift3+bstmShift3
    plmbsstay3 = bsaStay3+bsbafmStay3+bsbammStay3+bsbaomStay3+bsbahrmStay3+bsbabeStay3+bsentreStay3+bsremStay3+bshmStay3+bstmStay3
    #4th Year PLMBS
    plmbsshift4 = bsaShift4+bsbafmShift4+bsbammShift4+bsbaomShift4+bsbahrmShift4+bsbabeShift4+bsentreShift4+bsremShift4+bshmShift4+bstmShift4
    plmbsstay4 = bsaStay4+bsbafmStay4+bsbammStay4+bsbaomStay4+bsbahrmStay4+bsbabeStay4+bsentreStay4+bsremStay4+bshmStay4+bstmStay4
    #5th Year PLMBS
    plmbsshift5 = bsaShift5+bsbafmShift5+bsbammShift5+bsbaomShift5+bsbahrmShift5+bsbabeShift5+bsentreShift5+bsremShift5+bshmShift5+bstmShift5
    plmbsstay5 = bsaStay5+bsbafmStay5+bsbammStay5+bsbaomStay5+bsbahrmStay5+bsbabeStay5+bsentreStay5+bsremStay5+bshmStay5+bstmStay5
    #6th Year PLMBS
    plmbsshift6 = bsaShift6+bsbafmShift6+bsbammShift6+bsbaomShift6+bsbahrmShift6+bsbabeShift6+bsentreShift6+bsremShift6+bshmShift6+bstmShift6
    plmbsstay6 = bsaStay6+bsbafmStay6+bsbammStay6+bsbaomStay6+bsbahrmStay6+bsbabeStay6+bsentreStay6+bsremStay6+bshmStay6+bstmStay6
    #Whole PLMBS
    plmbsshift = plmbsshift1+plmbsshift2+plmbsshift3+plmbsshift4+plmbsshift5+plmbsshift6
    plmbsstay = plmbsstay1+plmbsstay2+plmbsstay3+plmbsstay4+plmbsstay5+plmbsstay6
    
    context = {
        'page':'dashboard',
        'student':student,
        'first_year':first_year.count(),
        'second_year':second_year.count(),
        'third_year':third_year.count(),
        'fourth_year':fourth_year.count(),
        'fifth_year':fifth_year.count(),
        'sixth_year':sixth_year.count(),
        'gender_male':gender_male.count(),
        'gender_female':gender_female.count(),
        'user':user,
        'current_datetime':current_datetime,
        'cetGenderM':cetGenderM,
        'cetGenderF':cetGenderF,
        'cetFirstYr':cetFirstYr,
        'cetSecondYr':cetSecondYr,
        'cetThirdYr':cetThirdYr,
        'cetFourthYr':cetFourthYr,
        'cetFifthYr':cetFifthYr,
        'cetSixthYr':cetSixthYr,
        'plmbsGenderM':plmbsGenderM,
        'plmbsGenderF':plmbsGenderF,
        'plmbsFirstYr':plmbsFirstYr,
        'plmbsSecondYr':plmbsSecondYr,
        'plmbsThirdYr':plmbsThirdYr,
        'plmbsFourthYr':plmbsFourthYr,
        'plmbsFifthYr':plmbsFifthYr,
        'plmbsSixthYr':plmbsSixthYr,
        #CET
        #CET Year Level
        'cetshift1':cetshift1,
        'cetshift2':cetshift2,
        'cetshift3':cetshift3,
        'cetshift4':cetshift4,
        'cetshift5':cetshift5,
        'cetshift6':cetshift6,
        'cetstay1':cetstay1,
        'cetstay2':cetstay2,
        'cetstay3':cetstay3,
        'cetstay4':cetstay4,
        'cetstay5':cetstay5,
        'cetstay6':cetstay6,
        #BSIT
        'bsitShift1': bsitShift1,
        'bsitShift2': bsitShift2,
        'bsitShift3': bsitShift3,
        'bsitShift4': bsitShift4,
        'bsitShift5': bsitShift5,
        'bsitShift6': bsitShift6,
        'bsitStay1': bsitStay1,
        'bsitStay2': bsitStay2,
        'bsitStay3': bsitStay3,
        'bsitStay4': bsitStay4,
        'bsitStay5': bsitStay5,
        'bsitStay6': bsitStay6,
        'bsitShift': bsitShift,
        'bsitStay': bsitStay,
        #BSCS
        'bscsShift1': bscsShift1,
        'bscsShift2': bscsShift2,
        'bscsShift3': bscsShift3,
        'bscsShift4': bscsShift4,
        'bscsShift5': bscsShift5,
        'bscsShift6': bscsShift6,
        'bscsStay1': bscsStay1,
        'bscsStay2': bscsStay2,
        'bscsStay3': bscsStay3,
        'bscsStay4': bscsStay4,
        'bscsStay5': bscsStay5,
        'bscsStay6': bscsStay6,
        'bsitShift': bsitShift,
        'bscsShift': bscsShift,
        'bscsStay': bscsStay,
        #BSCHE
        'bscheShift1': bscheShift1,
        'bscheShift2': bscheShift2,
        'bscheShift3': bscheShift3,
        'bscheShift4': bscheShift4,
        'bscheShift5': bscheShift5,
        'bscheShift6': bscheShift6,
        'bscheStay1': bscheStay1,
        'bscheStay2': bscheStay2,
        'bscheStay3': bscheStay3,
        'bscheStay4': bscheStay4,
        'bscheStay5': bscheStay5,
        'bscheStay6': bscheStay6,
        'bscheShift': bscheShift,
        'bscheStay': bscheStay,
        #BSCE
        'bsceShift1': bsceShift1,
        'bsceShift2': bsceShift2,
        'bsceShift3': bsceShift3,
        'bsceShift4': bsceShift4,
        'bsceShift5': bsceShift5,
        'bsceShift6': bsceShift6,
        'bsceStay1': bsceStay1,
        'bsceStay2': bsceStay2,
        'bsceStay3': bsceStay3,
        'bsceStay4': bsceStay4,
        'bsceStay5': bsceStay5,
        'bsceStay6': bsceStay6,
        'bsceShift': bsceShift,
        'bsceStay': bsceStay,
        #BSCpE
        'bscpeShift1': bscpeShift1,
        'bscpeShift2': bscpeShift2,
        'bscpeShift3': bscpeShift3,
        'bscpeShift4': bscpeShift4,
        'bscpeShift5': bscpeShift5,
        'bscpeShift6': bscpeShift6,
        'bscpeStay1': bscpeStay1,
        'bscpeStay2': bscpeStay2,
        'bscpeStay3': bscpeStay3,
        'bscpeStay4': bscpeStay4,
        'bscpeStay5': bscpeStay5,
        'bscpeStay6': bscpeStay6,
        'bscpeShift': bscpeShift,
        'bscpeStay': bscpeStay,
        #BSEE
        'bseeShift1': bseeShift1,
        'bseeShift2': bseeShift2,
        'bseeShift3': bseeShift3,
        'bseeShift4': bseeShift4,
        'bseeShift5': bseeShift5,
        'bseeShift6': bseeShift6,
        'bseeStay1': bseeStay1,
        'bseeStay2': bseeStay2,
        'bseeStay3': bseeStay3,
        'bseeStay4': bseeStay4,
        'bseeStay5': bseeStay5,
        'bseeStay6': bseeStay6,
        'bseeShift': bseeShift,
        'bseeStay': bseeStay,
        #BSECE
        'bseceShift1': bseceShift1,
        'bseceShift2': bseceShift2,
        'bseceShift3': bseceShift3,
        'bseceShift4': bseceShift4,
        'bseceShift5': bseceShift5,
        'bseceShift6': bseceShift6,
        'bseceStay1': bseceStay1,
        'bseceStay2': bseceStay2,
        'bseceStay3': bseceStay3,
        'bseceStay4': bseceStay4,
        'bseceStay5': bseceStay5,
        'bseceStay6': bseceStay6,
        'bseceShift': bseceShift,
        'bseceStay': bseceStay,
        #BSME
        'bsmeShift1': bsmeShift1,
        'bsmeShift2': bsmeShift2,
        'bsmeShift3': bsmeShift3,
        'bsmeShift4': bsmeShift4,
        'bsmeShift5': bsmeShift5,
        'bsmeShift6': bsmeShift6,
        'bsmeStay1': bsmeStay1,
        'bsmeStay2': bsmeStay2,
        'bsmeStay3': bsmeStay3,
        'bsmeStay4': bsmeStay4,
        'bsmeStay5': bsmeStay5,
        'bsmeStay6': bsmeStay6,
        'bsmeShift': bsmeShift,
        'bsmeStay': bsmeStay,
        #BSMfgE
        'bsmfgeShift1': bsmfgeShift1,
        'bsmfgeShift2': bsmfgeShift2,
        'bsmfgeShift3': bsmfgeShift3,
        'bsmfgeShift4': bsmfgeShift4,
        'bsmfgeShift5': bsmfgeShift5,
        'bsmfgeShift6': bsmfgeShift6,
        'bsmfgeStay1': bsmfgeStay1,
        'bsmfgeStay2': bsmfgeStay2,
        'bsmfgeStay3': bsmfgeStay3,
        'bsmfgeStay4': bsmfgeStay4,
        'bsmfgeStay5': bsmfgeStay5,
        'bsmfgeStay6': bsmfgeStay6,
        'bsmfgeShift': bsmfgeShift,
        'bsmfgeStay': bsmfgeStay,
        #Whole Cet
        'cetshift': cetshift,
        'cetstay': cetstay,
        #PLMBS
        #PLMBS Year Level
        'plmbsshift1':plmbsshift1,
        'plmbsshift2':plmbsshift2,
        'plmbsshift3':plmbsshift3,
        'plmbsshift4':plmbsshift4,
        'plmbsshift5':plmbsshift5,
        'plmbsshift6':plmbsshift6,
        'plmbsstay1':plmbsstay1,
        'plmbsstay2':plmbsstay2,
        'plmbsstay3':plmbsstay3,
        'plmbsstay4':plmbsstay4,
        'plmbsstay5':plmbsstay5,
        'plmbsstay6':plmbsstay6,
        #BSA
        'bsaShift1': bsaShift1,
        'bsaShift2': bsaShift2,
        'bsaShift3': bsaShift3,
        'bsaShift4': bsaShift4,
        'bsaShift5': bsaShift5,
        'bsaShift6': bsaShift6,
        'bsaStay1': bsaStay1,
        'bsaStay2': bsaStay2,
        'bsaStay3': bsaStay3,
        'bsaStay4': bsaStay4,
        'bsaStay5': bsaStay5,
        'bsaStay6': bsaStay6,
        'bsaShift': bsaShift,
        'bsaStay': bsaStay,
        #BSBA FM
        'bsbafmShift1': bsbafmShift1,
        'bsbafmShift2': bsbafmShift2,
        'bsbafmShift3': bsbafmShift3,
        'bsbafmShift4': bsbafmShift4,
        'bsbafmShift5': bsbafmShift5,
        'bsbafmShift6': bsbafmShift6,
        'bsbafmStay1': bsbafmStay1,
        'bsbafmStay2': bsbafmStay2,
        'bsbafmStay3': bsbafmStay3,
        'bsbafmStay4': bsbafmStay4,
        'bsbafmStay5': bsbafmStay5,
        'bsbafmStay6': bsbafmStay6,
        'bsbafmShift': bsbafmShift,
        'bsbafmStay': bsbafmStay,
        #BSBA MM
        'bsbammShift1': bsbammShift1,
        'bsbammShift2': bsbammShift2,
        'bsbammShift3': bsbammShift3,
        'bsbammShift4': bsbammShift4,
        'bsbammShift5': bsbammShift5,
        'bsbammShift6': bsbammShift6,
        'bsbammStay1': bsbammStay1,
        'bsbammStay2': bsbammStay2,
        'bsbammStay3': bsbammStay3,
        'bsbammStay4': bsbammStay4,
        'bsbammStay5': bsbammStay5,
        'bsbammStay6': bsbammStay6,
        'bsbammShift': bsbammShift,
        'bsbammStay': bsbammStay,
        #BSBA OM
        'bsbaomShift1': bsbaomShift1,
        'bsbaomShift2': bsbaomShift2,
        'bsbaomShift3': bsbaomShift3,
        'bsbaomShift4': bsbaomShift4,
        'bsbaomShift5': bsbaomShift5,
        'bsbaomShift6': bsbaomShift6,
        'bsbaomStay1': bsbaomStay1,
        'bsbaomStay2': bsbaomStay2,
        'bsbaomStay3': bsbaomStay3,
        'bsbaomStay4': bsbaomStay4,
        'bsbaomStay5': bsbaomStay5,
        'bsbaomStay6': bsbaomStay6,
        'bsbaomShift': bsbaomShift,
        'bsbaomStay': bsbaomStay,
        #BSBA HRM
        'bsbahrmShift1': bsbahrmShift1,
        'bsbahrmShift2': bsbahrmShift2,
        'bsbahrmShift3': bsbahrmShift3,
        'bsbahrmShift4': bsbahrmShift4,
        'bsbahrmShift5': bsbahrmShift5,
        'bsbahrmShift6': bsbahrmShift6,
        'bsbahrmStay1': bsbahrmStay1,
        'bsbahrmStay2': bsbahrmStay2,
        'bsbahrmStay3': bsbahrmStay3,
        'bsbahrmStay4': bsbahrmStay4,
        'bsbahrmStay5': bsbahrmStay5,
        'bsbahrmStay6': bsbahrmStay6,
        'bsbahrmShift': bsbahrmShift,
        'bsbahrmStay': bsbahrmStay,
        #BSBA BE
        'bsbabeShift1': bsbabeShift1,
        'bsbabeShift2': bsbabeShift2,
        'bsbabeShift3': bsbabeShift3,
        'bsbabeShift4': bsbabeShift4,
        'bsbabeShift5': bsbabeShift5,
        'bsbabeShift6': bsbabeShift6,
        'bsbabeStay1': bsbabeStay1,
        'bsbabeStay2': bsbabeStay2,
        'bsbabeStay3': bsbabeStay3,
        'bsbabeStay4': bsbabeStay4,
        'bsbabeStay5': bsbabeStay5,
        'bsbabeStay6': bsbabeStay6,
        'bsbabeShift': bsbabeShift,
        'bsbabeStay': bsbabeStay,
        #BS Entre
        'bsentreShift1': bsentreShift1,
        'bsentreShift2': bsentreShift2,
        'bsentreShift3': bsentreShift3,
        'bsentreShift4': bsentreShift4,
        'bsentreShift5': bsentreShift5,
        'bsentreShift6': bsentreShift6,
        'bsentreStay1': bsentreStay1,
        'bsentreStay2': bsentreStay2,
        'bsentreStay3': bsentreStay3,
        'bsentreStay4': bsentreStay4,
        'bsentreStay5': bsentreStay5,
        'bsentreStay6': bsentreStay6,
        'bsentreShift': bsentreShift,
        'bsentreStay': bsentreStay,
        #BS REM
        'bsremShift1': bsremShift1,
        'bsremShift2': bsremShift2,
        'bsremShift3': bsremShift3,
        'bsremShift4': bsremShift4,
        'bsremShift5': bsremShift5,
        'bsremShift6': bsremShift6,
        'bsremStay1': bsremStay1,
        'bsremStay2': bsremStay2,
        'bsremStay3': bsremStay3,
        'bsremStay4': bsremStay4,
        'bsremStay5': bsremStay5,
        'bsremStay6': bsremStay6,
        'bsremShift': bsremShift,
        'bsremStay': bsremStay,
        #BS HM
        'bshmShift1': bshmShift1,
        'bshmShift2': bshmShift2,
        'bshmShift3': bshmShift3,
        'bshmShift4': bshmShift4,
        'bshmShift5': bshmShift5,
        'bshmShift6': bshmShift6,
        'bshmStay1': bshmStay1,
        'bshmStay2': bshmStay2,
        'bshmStay3': bshmStay3,
        'bshmStay4': bshmStay4,
        'bshmStay5': bshmStay5,
        'bshmStay6': bshmStay6,
        'bshmShift': bshmShift,
        'bshmStay': bshmStay,
        #BS TM
        'bstmShift1': bstmShift1,
        'bstmShift2': bstmShift2,
        'bstmShift3': bstmShift3,
        'bstmShift4': bstmShift4,
        'bstmShift5': bstmShift5,
        'bstmShift6': bstmShift6,
        'bstmStay1': bstmStay1,
        'bstmStay2': bstmStay2,
        'bstmStay3': bstmStay3,
        'bstmStay4': bstmStay4,
        'bstmStay5': bstmStay5,
        'bstmStay6': bstmStay6,
        'bstmShift': bstmShift,
        'bstmStay': bstmStay,
        #Whole PLMBS
        'plmbsshift': plmbsshift,
        'plmbsstay': plmbsstay,
    }

    return render(request, 'dashboard.html', context)