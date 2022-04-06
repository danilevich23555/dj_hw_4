from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    student_object = Student.objects.all()
    for student in student_object:
        for teacher in student.teachers.all():
            print(teacher)
    context = {
        'object_list': student_object
    }
    ordering = 'group'

    return render(request, template, context)
