from django.urls import path

from courses import views

urlpatterns = [
    path('', views.show_courses, name='courses'),
    path('single/<id>', views.show_single_course, name='single_course')
]