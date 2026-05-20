from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('academic/', views.academic, name='academic'),

    path('gallery/', views.gallery, name='gallery'),

    path('contact/', views.contact, name='contact'),

    path('feespyment/', views.feespyment, name='feespyment'),

    path('readmore/', views.readmore, name='readmore'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('administration/', views.administration, name='administration'),

    path('student/', views.student, name='student'),

    path('teacher/', views.teacher, name='teacher'),

    path('courses/', views.courses, name='courses'),

    path('facilities/', views.facilities, name='facilities'),

    path('result/', views.result, name='result'),

    path('studentlogin/', views.studentlogin, name='studentlogin'),


]