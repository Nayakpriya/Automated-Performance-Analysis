
from .models import Question,Marks
from django.contrib import messages,auth
from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import Questionform
from .forms import Marksform
from .utils import suggested_questions
import json
def home(request):
    return render(request,'home.html')

def question_add(request):
    c_form = Questionform()

    if request.POST:
        c_form = Questionform(request.POST)
        if c_form.is_valid():
            c_form.save()
            messages.success(request,'The question is added')
            return redirect('question-add')
    return render(request, 'create.html', context={'form':c_form, 'button_text': 'Add Question'})


def login(request):
    if request.POST:
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name, password=password)

        if user is not None:
            auth.login(request, user)
            if request.user.is_superuser:
                messages.success(request,'Logged in as teacher')
                return redirect('admin/')
            else:
                messages.success(request, 'Logged in as a student')
                return redirect('suggested-list')
        else:
            messages.warning(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


def marks_add(request):
    c_form = Marksform()

    if request.POST:
        c_form = Marksform(request.POST)
        if c_form.is_valid():
            c_form.save()
            messages.success(request,'The question is added')
            return redirect('question-add')
    return render(request, 'create.html', context={'form':c_form, 'button_text': 'Add Student Details'})


def marks_details(request):
    marks=Marks.objects.all()
    context={
        'title':'Marks Details',
        'data':marks
    }
    return render(request,'table.html',context=context)


def marks_charts_1(request):
    d1=0
    d5=0
    d2=0
    d3=0
    d4=0
    data=Marks.objects.filter(test='1')
    for d in data:
        if 10>=d.total:
            d1+=1
        if 10<d.total<=20:
            d2+=1
        if 20<d.total<=30:
            d3+=1
        if 30<d.total<=40:
            d4+=1
        if 40<d.total<=50:
            d5+=1
    
    labels=[d1,d2,d3,d4,d5]
    print(labels)
    context={
           
            "data":data,
            "labels":labels,
        }
    return render(request,'index.html',context=context)

def marks_charts_2(request):
    d1=0
    d5=0
    d2=0
    d3=0
    d4=0
    data=Marks.objects.filter(test='2')
    for d in data:
        if 10>=d.total:
            d1+=1
        if 10<d.total<=20:
            d2+=1
        if 20<d.total<=30:
            d3+=1
        if 30<d.total<=40:
            d4+=1
        if 40<d.total<=50:
            d5+=1
    
    labels=[d1,d2,d3,d4,d5]
    print(labels)
    context={
           
            "data":data,
            "labels":labels,
        }
    return render(request,'index.html',context=context)

def marks_charts_3(request):
    d1=0
    d5=0
    d2=0
    d3=0
    d4=0
    data=Marks.objects.filter(test='3')
    for d in data:
        if 10>=d.total:
            d1+=1
        if 10<d.total<=20:
            d2+=1
        if 20<d.total<=30:
            d3+=1
        if 30<d.total<=40:
            d4+=1
        if 40<d.total<=50:
            d5+=1
    
    labels=[d1,d2,d3,d4,d5]
    print(labels)
    context={
           
            "data":data,
            "labels":labels,
        }
    return render(request,'index.html',context=context)

def suggested_list(request):
    marks=[]
    co=[]
    question=[]
    for element in suggested_questions:
        print(type(element))
        print(element)
        marks.append(element.get("Marks"))
        question.append(element.get("Question"))
        co.append(element.get("COs"))
    print(marks,question,co)
    data=zip(question,marks,co)
    context={
      "data":data
    }
    
    return render(request,'suggested.html',context=context)
