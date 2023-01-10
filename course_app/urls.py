
from django.contrib import admin
from django.urls import path
from .views import CourseListView,CourseDetailView
app_name = 'course_app'
urlpatterns = [
    path('',CourseListView.as_view(),name="list"),

   path('<slug>',CourseDetailView.as_view(),name='detail')
    
]