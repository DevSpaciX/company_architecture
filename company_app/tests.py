from django.test import TestCase
from django.shortcuts import render
from company_app.models import Employee

def employee_tree(request):
    employees = Employee.objects.all()
    return render(request, 'employee_tree.html', {'employees': employees})
