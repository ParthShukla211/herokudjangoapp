from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('', views.index , name='home'),
    path('myskills/', views.myskills , name='myskills'),
    path('myprojects/', views.myprojects , name='myprojects'),
    path('certificates/', views.certificates , name='certificates'),
    path('aboutme/', views.aboutme , name='aboutme'),
    path('contactme', views.contactme , name='contactme'),
    path('downloadresume/', views.download_resume_file, name='download_resume_file'),
    path('downloadcv/', views.download_cv_file, name='download_cv_file')
]