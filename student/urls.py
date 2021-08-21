from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('question-add/',question_add,name="question-add"),
    path('login/',login,name="login"),
    path('marks-add',marks_add,name="marks-add"),
    path('marks-charts',marks_charts,name="marks-charts"),
    path('marks-details',marks_details,name='marks-details'),
]
