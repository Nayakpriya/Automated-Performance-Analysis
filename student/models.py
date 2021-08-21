

from django.db import models
from django.contrib.auth.models import User

import datetime



class Question(models.Model):
    topic = models.CharField(max_length=500,null=True, blank=True )
    question= models.CharField(max_length=1000,null=True, blank=True,verbose_name='Question')
    course_outcomes=models.CharField(max_length=500, null=True, blank=True,)
    test=models.CharField(max_length=500, null=True, blank=True,verbose_name='Test number')
    date = models.DateField(blank=True, null=True, default=datetime.date.today)

    def __str__(self):
        return self.question


class Marks(models.Model):
    student_name = models.CharField(max_length=500,null=True, blank=True )
    usn=models.CharField(max_length=500,null=True, blank=True )
    test= models.CharField(max_length=1000,null=True, blank=True,verbose_name='Test number')
    q1=models.IntegerField( null=True, blank=True,verbose_name='Question 1 Marks')
    q2=models.IntegerField( null=True, blank=True,verbose_name='Question 2 Marks')
    q3=models.IntegerField( null=True, blank=True,verbose_name='Question 3 Marks')
    q4=models.IntegerField( null=True, blank=True,verbose_name='Question 4 Marks')
    q5=models.IntegerField( null=True, blank=True,verbose_name='Question 5 Marks')
    total=models.IntegerField( null=True, blank=True,verbose_name='Total')
    

    def __str__(self):
        return self.question