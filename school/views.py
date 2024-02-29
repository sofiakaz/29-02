from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    # Получаем список всех студентов и сортируем по классу
    students = Student.objects.order_by('group')

    context = {'students': students}
    print(context)
    return render(request, template, context)
