from django.db import models
from django.contrib.auth.models import AbstractUser

# class Department(models.Model):
#     departmentName = models.CharField(max_length=255, null=True)
#     is_inactive = models.BooleanField(default=False)

#     def __str__(self):
#         return '%s' %(self.departmentName)

class CustomUser(AbstractUser):
    course_list = [
        ('BS Information and Technology','BS Information and Technology'),
        ('BS Computer Science','BS Computer Science'),
        ('BS Chemical Engineering (BSCHE)','BS Chemical Engineering (BSCHE)'),
        ('BS Civil Engineering (BSCE)','BS Civil Engineering (BSCE)'),
        ('BS Computer Engineering (BSCpE)','BS Computer Engineering (BSCpE)'),
        ('BS Electrical Engineering (BSEE)','BS Electrical Engineering (BSEE)'),
        ('BS Electronics Engineering (BSECE)','BS Electronics Engineering (BSECE)'),
        ('BS Mechanical Engineering (BSME)','BS Mechanical Engineering (BSME)'),
        ('BS Manufacturing Engineering (BSMfgE)','BS Manufacturing Engineering (BSMfgE)'),
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

        ('Bachelor of Science in Architecture - BS Arch','Bachelor of Science in Architecture - BS Arch'),

        ('Bachelor of Elementary Education (Generalist) (BEEd)','Bachelor of Elementary Education (Generalist) (BEEd)'),
        ('Bachelor of Secondary Education major in English (BSEd-Eng)','Bachelor of Secondary Education major in English (BSEd-Eng)'),
        ('Bachelor of Secondary Education major in Filipino (BSEd-Fil)','Bachelor of Secondary Education major in Filipino (BSEd-Fil)'),
        ('Bachelor of Secondary Education major Mathematics (BSEd-Math)','Bachelor of Secondary Education major Mathematics (BSEd-Math)'),
        ('Bachelor of Secondary Education major in Sciences (BSEd-Sciences)','Bachelor of Secondary Education major in Sciences (BSEd-Sciences)'),
        ('Bachelor of Secondary Education major in Social Studies (BSEd-SS)','Bachelor of Secondary Education major in Social Studies (BSEd-SS)'),
        ('Bachelor of Physical Education (BPE)','Bachelor of Physical Education (BPE)'),

        ('Bachelor of Arts in Communication - BAC','Bachelor of Arts in Communication - BAC'),
        ('Bachelor of Arts in Communication Major in Public Relations - BAC-PR','Bachelor of Arts in Communication Major in Public Relations - BAC-PR'),
        ('Bachelor of Arts in Public Relations - BAPR','Bachelor of Arts in Public Relations - BAPR'),

        ('Bachelor of Science in Social Work - BS SW','Bachelor of Science in Social Work - BS SW'),

         ('Bachelor of Science in Physical Therapy - BSPT','Bachelor of Science in Physical Therapy - BSPT'),

        ('Bachelor of Science in Nursing - BSN','Bachelor of Science in Nursing - BSN'),

        ('Bachelor of Science in Biology - BS Bio','Bachelor of Science in Biology - BS Bio'),
        ('Bachelor of Science in Psychology - BS PSY','Bachelor of Science in Psychology - BS PSY'),
        ('Bachelor of Science in Chemistry - BS Chem','Bachelor of Science in Chemistry - BS Chem'),

        ('Bachelor of Science in Mathematics - BS Math','Bachelor of Science in Mathematics - BS Math'),

    ]
    type = [
        ('Administrator', 'Administrator'),
        ('Chairperson', 'Chairperson'),
        ('Dean', 'Dean'),
    ]
    department_list = [
        ('College of Engineering','College of Engineering'),
        ('PLM Business School','PLM Business School'),
        ('College of Architecture and Urban Planning','College of Architecture and Urban Planning'),
        ('College of Education','College of Education'),
        ('College of Humanities, Arts, and Social Sciences','College of Humanities, Arts, and Social Sciences'),
        ('College of Physical Therapy','College of Physical Therapy'),
        ('College of Nursing','College of Nursing'),
        ('College of Science','College of Science'),

    ]
    first_name = models.CharField(max_length=50, verbose_name="First Name", null=True)
    last_name = models.CharField(max_length=50, verbose_name="Last Name", null=True)
    department = models.CharField(choices=department_list, max_length=50, verbose_name="Department", blank=True, null=True)
    contactNumber = models.CharField(max_length=12, verbose_name="Contact Number", blank=True, default='')
    accountType = models.CharField(choices=type, max_length=50, verbose_name="Account Type", blank=True, default='')
    college = models.CharField(choices=course_list, max_length=150, verbose_name="College", blank=True, null=True)
    date_of_inactivity = models.DateTimeField(blank=True, null=True)

class Student(models.Model):
    course = [
        #College of Engineering and Technology
        ('BS Information and Technology','BS Information and Technology'),
        ('BS Computer Science','BS Computer Science'),
        ('BS Chemical Engineering (BSCHE)','BS Chemical Engineering (BSCHE)'),
        ('BS Civil Engineering (BSCE)','BS Civil Engineering (BSCE)'),
        ('BS Computer Engineering (BSCpE)','BS Computer Engineering (BSCpE)'),
        ('BS Electrical Engineering (BSEE)','BS Electrical Engineering (BSEE)'),
        ('BS Electronics Engineering (BSECE)','BS Electronics Engineering (BSECE)'),
        ('BS Mechanical Engineering (BSME)','BS Mechanical Engineering (BSME)'),
        ('BS Manufacturing Engineering (BSMfgE)','BS Manufacturing Engineering (BSMfgE)'),
        #PLM Business School
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
        #College of Architecture and Urban Planning
        ('Bachelor of Science in Architecture - BS Arch','Bachelor of Science in Architecture - BS Arch'),
        #College of Education
        ('Bachelor of Elementary Education (Generalist) (BEEd)','Bachelor of Elementary Education (Generalist) (BEEd)'),
        ('Bachelor of Secondary Education major in English (BSEd-Eng)','Bachelor of Secondary Education major in English (BSEd-Eng)'),
        ('Bachelor of Secondary Education major in Filipino (BSEd-Fil)','Bachelor of Secondary Education major in Filipino (BSEd-Fil)'),
        ('Bachelor of Secondary Education major Mathematics (BSEd-Math)','Bachelor of Secondary Education major Mathematics (BSEd-Math)'),
        ('Bachelor of Secondary Education major in Sciences (BSEd-Sciences)','Bachelor of Secondary Education major in Sciences (BSEd-Sciences)'),
        ('Bachelor of Secondary Education major in Social Studies (BSEd-SS)','Bachelor of Secondary Education major in Social Studies (BSEd-SS)'),
        ('Bachelor of Physical Education (BPE)','Bachelor of Physical Education (BPE)'),
        #College of Humanities, Arts, and Social Sciences
        ('Bachelor of Arts in Communication - BAC','Bachelor of Arts in Communication - BAC'),
        ('Bachelor of Arts in Communication Major in Public Relations - BAC-PR','Bachelor of Arts in Communication Major in Public Relations - BAC-PR'),
        ('Bachelor of Arts in Public Relations - BAPR','Bachelor of Arts in Public Relations - BAPR'),
        ('Bachelor of Science in Social Work - BS SW','Bachelor of Science in Social Work - BS SW'),
        #College of Physical Therapy
        ('Bachelor of Science in Physical Therapy - BSPT','Bachelor of Science in Physical Therapy - BSPT'),
        #College of Nursing
        ('Bachelor of Science in Nursing - BSN','Bachelor of Science in Nursing - BSN'),
        #College of Science
        ('Bachelor of Science in Biology - BS Bio','Bachelor of Science in Biology - BS Bio'),
        ('Bachelor of Science in Psychology - BS PSY','Bachelor of Science in Psychology - BS PSY'),
        ('Bachelor of Science in Chemistry - BS Chem','Bachelor of Science in Chemistry - BS Chem'),
        ('Bachelor of Science in Mathematics - BS Math','Bachelor of Science in Mathematics - BS Math'),
    ]
    gwa = [
        ('1.00-1.50',1),
        ('1.51-2.00',2),
        ('2.01-2.50',3),
        ('2.51-3.00',4),
        ('N/A',0),
    ]
    strand = [
        ('Technical-Vocational-Livelihood','Technical-Vocational-Livelihood'),
        ('Sports and Arts','Sports and Arts'),
        ('Accountancy, Business, Management (ABM)','Accountancy, Business, Management (ABM)'),
        ('Humanities, Education, Social Sciences (HESS)','Humanities, Education, Social Sciences (HESS)'),
        ('Science, Technology, Engineering, Mathematics (STEM)','Science, Technology, Engineering, Mathematics (STEM)'),

    ]
    no_of_stud = [
        ('10-30',1),
        ('31-50',2),
        ('51-70',3),
        ('70+',4),
    ]
    who_decided = [
        ('Myself',1),
        ('Family',2),
        ('Friends and/or boyfriend/girlfriend',3),
        ('Institution',4),
        ('Teachers',5),
        ('Others',6),
    ]
    who_influcenced = [
        ('Myself',1),
        ('Family',2),
        ('Friends and/or boyfriend/girlfriend',3),
        ('Institution',4),
        ('Teachers',5),
        ('Professionals',6),
        ('Socioeconomic',7),
        ('Others',8),
    ]
    year = [
        ('1st Year',1),
        ('2nd Year',2),
        ('3rd Year',3),
        ('4th Year',4),
        ('5th Year',5),
        ('6th Year',6)
    ]
    first_name = models.CharField(max_length=50, verbose_name="First Name", null=True)
    last_name = models.CharField(max_length=50, verbose_name="Last Name", null=True)
    gender = models.CharField(max_length=50, verbose_name="Gender", null=True)
    current_year = models.CharField(max_length=100, verbose_name="Current Year", null=True)
    current_college = models.CharField(max_length=100, verbose_name="Current College", null=True)
    #SHS Strand
    shs_strand = models.CharField(choices=strand, max_length=100, verbose_name="SHS Strand", null=True)
    #Course Choice
    first_choice = models.CharField(choices=course, max_length=100, verbose_name="First Choice", null=True)
    second_choice = models.CharField(choices=course, max_length=100, verbose_name="Second Choice", null=True)
    third_choice = models.CharField(choices=course, max_length=100, verbose_name="Third Choice", null=True)
    current_course =  models.CharField(choices=course, max_length=100, verbose_name="Current Course", null=True)
    #Course Decision Question
    decision_making1 = models.IntegerField(verbose_name="Decision Making 1", null=True)
    decision_making2 = models.IntegerField(verbose_name="Decision Making 2", null=True)
    decision_making3 = models.IntegerField(verbose_name="Decision Making 3", null=True)
    decision_making4 = models.IntegerField(verbose_name="Decision Making 4", null=True)
    decision_making5 = models.IntegerField(verbose_name="Decision Making 5", null=True)
    #Personal Assessment Question
    personal_assessment1 = models.IntegerField(verbose_name="Personal Assessment 1", null=True)
    personal_assessment2 = models.IntegerField(verbose_name="Personal Assessment 2", null=True)
    personal_assessment3 = models.IntegerField(verbose_name="Personal Assessment 3", null=True)
    personal_assessment4 = models.IntegerField(verbose_name="Personal Assessment 4", null=True)
    personal_assessment5 = models.IntegerField(verbose_name="Personal Assessment 5", null=True)
    #Course Enviroment Question
    course_enviroment1 = models.IntegerField(verbose_name="Course Enviroment 1", null=True)
    course_enviroment2 = models.IntegerField(verbose_name="Course Enviroment 2", null=True)
    course_enviroment3 = models.IntegerField(verbose_name="Course Enviroment 3", null=True)
    course_enviroment4 = models.IntegerField(verbose_name="Course Enviroment 4", null=True)
    course_enviroment5 = models.IntegerField(verbose_name="Course Enviroment 5", null=True)
    #Course Satisfaction Question
    course_satisfaction1 = models.IntegerField(verbose_name="Course Satisfaction 1", null=True)
    course_satisfaction2 = models.IntegerField(verbose_name="Course Satisfaction 2", null=True)
    course_satisfaction3 = models.IntegerField(verbose_name="Course Satisfaction 3", null=True)
    course_satisfaction4 = models.IntegerField(verbose_name="Course Satisfaction 4", null=True)
    course_satisfaction5 = models.IntegerField(verbose_name="Course Satisfaction 5", null=True)
    #Academic Experience Question
    academic_experience1 = models.IntegerField(verbose_name="Academic Experience 1", null=True)
    academic_experience2 = models.IntegerField(verbose_name="Academic Experience 2", null=True)
    academic_experience3 = models.IntegerField(verbose_name="Academic Experience 3", null=True)
    academic_experience4 = models.IntegerField(verbose_name="Academic Experience 4", null=True)
    academic_experience5 = models.IntegerField(verbose_name="Academic Experience 5", null=True)
    #Result
    result = models.FloatField(verbose_name="Result", null=True)
    #willshift
    shiftDecision = models.IntegerField(verbose_name="Shift Decision", null=True)
    def __str__(self):
        return '%s, %s' %(self.last_name, self.first_name)
