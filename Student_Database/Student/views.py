# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .models import Student

# Create your views here.

@login_required(login_url="/Student/login/")
def student(request):
	student_info = {}
	return render(request, 'student.html', student_info)
	
