from django.shortcuts import render
from django.views.generic import TemplateView


class NewJoinEmployeeCreate(TemplateView):
    template_name = "hr_department/page_1_hr.html"