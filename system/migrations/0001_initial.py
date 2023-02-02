# Generated by Django 4.1.1 on 2022-11-30 14:12

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='Last Name')),
                ('gender', models.CharField(max_length=50, null=True, verbose_name='Gender')),
                ('current_year', models.CharField(max_length=100, null=True, verbose_name='Current Year')),
                ('current_college', models.CharField(max_length=100, null=True, verbose_name='Current College')),
                ('shs_strand', models.CharField(choices=[('Technical-Vocational-Livelihood', 'Technical-Vocational-Livelihood'), ('Sports and Arts', 'Sports and Arts'), ('Accountancy, Business, Management (ABM)', 'Accountancy, Business, Management (ABM)'), ('Humanities, Education, Social Sciences (HESS)', 'Humanities, Education, Social Sciences (HESS)'), ('Science, Technology, Engineering, Mathematics (STEM)', 'Science, Technology, Engineering, Mathematics (STEM)')], max_length=100, null=True, verbose_name='SHS Strand')),
                ('first_choice', models.CharField(choices=[('BS Information and Technology', 'BS Information and Technology'), ('BS Computer Science', 'BS Computer Science'), ('BS Chemical Engineering (BSCHE)', 'BS Chemical Engineering (BSCHE)'), ('BS Civil Engineering (BSCE)', 'BS Civil Engineering (BSCE)'), ('BS Computer Engineering (BSCpE)', 'BS Computer Engineering (BSCpE)'), ('BS Electrical Engineering (BSEE)', 'BS Electrical Engineering (BSEE)'), ('BS Electronics Engineering (BSECE)', 'BS Electronics Engineering (BSECE)'), ('BS Mechanical Engineering (BSME)', 'BS Mechanical Engineering (BSME)'), ('BS Manufacturing Engineering (BSMfgE)', 'BS Manufacturing Engineering (BSMfgE)'), ('Bachelor of Science in Accountancy (BSA)', 'Bachelor of Science in Accountancy (BSA)'), ('Bachelor of Science in Business Administration major in Financial Management (BSBA FM)', 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)'), ('Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)', 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)'), ('Bachelor of Science in Business Administration major in Operations Management (BSBA OM)', 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)'), ('Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)', 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)'), ('Bachelor of Science in Business Administration major in Business Economics(BSBA BE)', 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)'), ('Bachelor of Science in Entrepreneurship (BS ENTRE)', 'Bachelor of Science in Entrepreneurship (BS ENTRE)'), ('Bachelor of Science in Real Estate Management (BSREM)', 'Bachelor of Science in Real Estate Management (BSREM)'), ('Bachelor of Science in Hospitality Management (BSHM)', 'Bachelor of Science in Hospitality Management (BSHM)'), ('Bachelor of Science in Tourism Management (BSTM)', 'Bachelor of Science in Tourism Management (BSTM)')], max_length=100, null=True, verbose_name='First Choice')),
                ('second_choice', models.CharField(choices=[('BS Information and Technology', 'BS Information and Technology'), ('BS Computer Science', 'BS Computer Science'), ('BS Chemical Engineering (BSCHE)', 'BS Chemical Engineering (BSCHE)'), ('BS Civil Engineering (BSCE)', 'BS Civil Engineering (BSCE)'), ('BS Computer Engineering (BSCpE)', 'BS Computer Engineering (BSCpE)'), ('BS Electrical Engineering (BSEE)', 'BS Electrical Engineering (BSEE)'), ('BS Electronics Engineering (BSECE)', 'BS Electronics Engineering (BSECE)'), ('BS Mechanical Engineering (BSME)', 'BS Mechanical Engineering (BSME)'), ('BS Manufacturing Engineering (BSMfgE)', 'BS Manufacturing Engineering (BSMfgE)'), ('Bachelor of Science in Accountancy (BSA)', 'Bachelor of Science in Accountancy (BSA)'), ('Bachelor of Science in Business Administration major in Financial Management (BSBA FM)', 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)'), ('Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)', 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)'), ('Bachelor of Science in Business Administration major in Operations Management (BSBA OM)', 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)'), ('Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)', 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)'), ('Bachelor of Science in Business Administration major in Business Economics(BSBA BE)', 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)'), ('Bachelor of Science in Entrepreneurship (BS ENTRE)', 'Bachelor of Science in Entrepreneurship (BS ENTRE)'), ('Bachelor of Science in Real Estate Management (BSREM)', 'Bachelor of Science in Real Estate Management (BSREM)'), ('Bachelor of Science in Hospitality Management (BSHM)', 'Bachelor of Science in Hospitality Management (BSHM)'), ('Bachelor of Science in Tourism Management (BSTM)', 'Bachelor of Science in Tourism Management (BSTM)')], max_length=100, null=True, verbose_name='Second Choice')),
                ('third_choice', models.CharField(choices=[('BS Information and Technology', 'BS Information and Technology'), ('BS Computer Science', 'BS Computer Science'), ('BS Chemical Engineering (BSCHE)', 'BS Chemical Engineering (BSCHE)'), ('BS Civil Engineering (BSCE)', 'BS Civil Engineering (BSCE)'), ('BS Computer Engineering (BSCpE)', 'BS Computer Engineering (BSCpE)'), ('BS Electrical Engineering (BSEE)', 'BS Electrical Engineering (BSEE)'), ('BS Electronics Engineering (BSECE)', 'BS Electronics Engineering (BSECE)'), ('BS Mechanical Engineering (BSME)', 'BS Mechanical Engineering (BSME)'), ('BS Manufacturing Engineering (BSMfgE)', 'BS Manufacturing Engineering (BSMfgE)'), ('Bachelor of Science in Accountancy (BSA)', 'Bachelor of Science in Accountancy (BSA)'), ('Bachelor of Science in Business Administration major in Financial Management (BSBA FM)', 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)'), ('Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)', 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)'), ('Bachelor of Science in Business Administration major in Operations Management (BSBA OM)', 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)'), ('Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)', 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)'), ('Bachelor of Science in Business Administration major in Business Economics(BSBA BE)', 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)'), ('Bachelor of Science in Entrepreneurship (BS ENTRE)', 'Bachelor of Science in Entrepreneurship (BS ENTRE)'), ('Bachelor of Science in Real Estate Management (BSREM)', 'Bachelor of Science in Real Estate Management (BSREM)'), ('Bachelor of Science in Hospitality Management (BSHM)', 'Bachelor of Science in Hospitality Management (BSHM)'), ('Bachelor of Science in Tourism Management (BSTM)', 'Bachelor of Science in Tourism Management (BSTM)')], max_length=100, null=True, verbose_name='Third Choice')),
                ('current_course', models.CharField(choices=[('BS Information and Technology', 'BS Information and Technology'), ('BS Computer Science', 'BS Computer Science'), ('BS Chemical Engineering (BSCHE)', 'BS Chemical Engineering (BSCHE)'), ('BS Civil Engineering (BSCE)', 'BS Civil Engineering (BSCE)'), ('BS Computer Engineering (BSCpE)', 'BS Computer Engineering (BSCpE)'), ('BS Electrical Engineering (BSEE)', 'BS Electrical Engineering (BSEE)'), ('BS Electronics Engineering (BSECE)', 'BS Electronics Engineering (BSECE)'), ('BS Mechanical Engineering (BSME)', 'BS Mechanical Engineering (BSME)'), ('BS Manufacturing Engineering (BSMfgE)', 'BS Manufacturing Engineering (BSMfgE)'), ('Bachelor of Science in Accountancy (BSA)', 'Bachelor of Science in Accountancy (BSA)'), ('Bachelor of Science in Business Administration major in Financial Management (BSBA FM)', 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)'), ('Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)', 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)'), ('Bachelor of Science in Business Administration major in Operations Management (BSBA OM)', 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)'), ('Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)', 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)'), ('Bachelor of Science in Business Administration major in Business Economics(BSBA BE)', 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)'), ('Bachelor of Science in Entrepreneurship (BS ENTRE)', 'Bachelor of Science in Entrepreneurship (BS ENTRE)'), ('Bachelor of Science in Real Estate Management (BSREM)', 'Bachelor of Science in Real Estate Management (BSREM)'), ('Bachelor of Science in Hospitality Management (BSHM)', 'Bachelor of Science in Hospitality Management (BSHM)'), ('Bachelor of Science in Tourism Management (BSTM)', 'Bachelor of Science in Tourism Management (BSTM)')], max_length=100, null=True, verbose_name='Current Course')),
                ('decision_making1', models.IntegerField(null=True, verbose_name='Decision Making 1')),
                ('decision_making2', models.IntegerField(null=True, verbose_name='Decision Making 2')),
                ('decision_making3', models.IntegerField(null=True, verbose_name='Decision Making 3')),
                ('decision_making4', models.IntegerField(null=True, verbose_name='Decision Making 4')),
                ('decision_making5', models.IntegerField(null=True, verbose_name='Decision Making 5')),
                ('personal_assessment1', models.IntegerField(null=True, verbose_name='Personal Assessment 1')),
                ('personal_assessment2', models.IntegerField(null=True, verbose_name='Personal Assessment 2')),
                ('personal_assessment3', models.IntegerField(null=True, verbose_name='Personal Assessment 3')),
                ('personal_assessment4', models.IntegerField(null=True, verbose_name='Personal Assessment 4')),
                ('personal_assessment5', models.IntegerField(null=True, verbose_name='Personal Assessment 5')),
                ('course_enviroment1', models.IntegerField(null=True, verbose_name='Course Enviroment 1')),
                ('course_enviroment2', models.IntegerField(null=True, verbose_name='Course Enviroment 2')),
                ('course_enviroment3', models.IntegerField(null=True, verbose_name='Course Enviroment 3')),
                ('course_enviroment4', models.IntegerField(null=True, verbose_name='Course Enviroment 4')),
                ('course_enviroment5', models.IntegerField(null=True, verbose_name='Course Enviroment 5')),
                ('course_satisfaction1', models.IntegerField(null=True, verbose_name='Course Satisfaction 1')),
                ('course_satisfaction2', models.IntegerField(null=True, verbose_name='Course Satisfaction 2')),
                ('course_satisfaction3', models.IntegerField(null=True, verbose_name='Course Satisfaction 3')),
                ('course_satisfaction4', models.IntegerField(null=True, verbose_name='Course Satisfaction 4')),
                ('course_satisfaction5', models.IntegerField(null=True, verbose_name='Course Satisfaction 5')),
                ('academic_experience1', models.IntegerField(null=True, verbose_name='Academic Experience 1')),
                ('academic_experience2', models.IntegerField(null=True, verbose_name='Academic Experience 2')),
                ('academic_experience3', models.IntegerField(null=True, verbose_name='Academic Experience 3')),
                ('academic_experience4', models.IntegerField(null=True, verbose_name='Academic Experience 4')),
                ('academic_experience5', models.IntegerField(null=True, verbose_name='Academic Experience 5')),
                ('result', models.FloatField(null=True, verbose_name='Result')),
                ('shiftDecision', models.IntegerField(null=True, verbose_name='Shift Decision')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='Last Name')),
                ('department', models.CharField(blank=True, choices=[('CET', 'CET'), ('PLMBS', 'PLMBS')], max_length=50, null=True, verbose_name='Department')),
                ('contactNumber', models.CharField(blank=True, default='', max_length=12, verbose_name='Contact Number')),
                ('accountType', models.CharField(blank=True, choices=[('Administrator', 'Administrator'), ('Chairperson', 'Chairperson'), ('Dean', 'Dean')], default='', max_length=50, verbose_name='Account Type')),
                ('college', models.CharField(blank=True, choices=[('BS Information and Technology', 'BS Information and Technology'), ('BS Computer Science', 'BS Computer Science'), ('BS Chemical Engineering (BSCHE)', 'BS Chemical Engineering (BSCHE)'), ('BS Civil Engineering (BSCE)', 'BS Civil Engineering (BSCE)'), ('BS Computer Engineering (BSCpE)', 'BS Computer Engineering (BSCpE)'), ('BS Electrical Engineering (BSEE)', 'BS Electrical Engineering (BSEE)'), ('BS Electronics Engineering (BSECE)', 'BS Electronics Engineering (BSECE)'), ('BS Mechanical Engineering (BSME)', 'BS Mechanical Engineering (BSME)'), ('BS Manufacturing Engineering (BSMfgE)', 'BS Manufacturing Engineering (BSMfgE)'), ('Bachelor of Science in Accountancy (BSA)', 'Bachelor of Science in Accountancy (BSA)'), ('Bachelor of Science in Business Administration major in Financial Management (BSBA FM)', 'Bachelor of Science in Business Administration major in Financial Management (BSBA FM)'), ('Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)', 'Bachelor of Science in Business Administration major in Marketing Management (BSBA MM)'), ('Bachelor of Science in Business Administration major in Operations Management (BSBA OM)', 'Bachelor of Science in Business Administration major in Operations Management (BSBA OM)'), ('Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)', 'Bachelor of Science in Business Administration major in Human Resource Management(BSBA HRM)'), ('Bachelor of Science in Business Administration major in Business Economics(BSBA BE)', 'Bachelor of Science in Business Administration major in Business Economics(BSBA BE)'), ('Bachelor of Science in Entrepreneurship (BS ENTRE)', 'Bachelor of Science in Entrepreneurship (BS ENTRE)'), ('Bachelor of Science in Real Estate Management (BSREM)', 'Bachelor of Science in Real Estate Management (BSREM)'), ('Bachelor of Science in Hospitality Management (BSHM)', 'Bachelor of Science in Hospitality Management (BSHM)'), ('Bachelor of Science in Tourism Management (BSTM)', 'Bachelor of Science in Tourism Management (BSTM)')], max_length=150, null=True, verbose_name='College')),
                ('date_of_inactivity', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]