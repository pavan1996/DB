# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models

# Create your models here.



class Student(models.Model):
	student_name	= models.CharField(max_length=50)
	usn 			= models.CharField(max_length=10, primary_key=True)		
	date_of_birth 	= models.DateField()
	address 		= models.CharField(max_length=50)
	contact_number 	= models.CharField(max_length=10)
	department 		= models.ForeignKey(
			'Department',
			on_delete=models.CASCADE,
		)


class Student_Course(models.Model):
	usn 			= models.ForeignKey(
			'Student',
			on_delete=models.CASCADE,
		)
	course 			= models.ForeignKey(
			'Student_Course',
			on_delete=models.CASCADE,
		)

class Department(models.Model):
	department_id   	= models.IntegerField(primary_key=True)
	department_name 	= models.CharField(max_length = 50)
	head_of_department 	= models.CharField(max_length=50)


class Course(models.Model):
	course_id 	= models.CharField(max_length=20, primary_key=True)
	course_name = models.CharField(max_length=50)
	department  = models.ForeignKey(
			'Department',
			on_delete=models.CASCADE,
		)

class Exam(models.Model):
	usn 			= models.ForeignKey(
			'Student',
			on_delete=models.CASCADE,
		)
	course 			= models.ForeignKey(
			'Course',
			on_delete=models.CASCADE,
		)
	marks 			= models.IntegerField()


class Attendance(models.Model):
	usn 			 = models.ForeignKey(
			'Student',
			on_delete=models.CASCADE,
		)
	course 			 = models.ForeignKey(
			'Course',
			on_delete=models.CASCADE,
		)
	percentage		 = models.IntegerField()