from django.urls import path
from .views import *

from . import views
import json
urlpatterns = [
    path('', views.home, name="home"),
    path('question-add/',question_add,name="question-add"),
    path('login/',login,name="login"),
    path('marks-add',marks_add,name="marks-add"),
    path('marks-charts-1',marks_charts_1,name="marks-charts-1"),
    path('marks-charts-2',marks_charts_2,name="marks-charts-2"),
    path('marks-charts-3',marks_charts_3,name="marks-charts-3"),
    path('report_1/', csv_export_1, name='csv-export-1'),
    path('report_2/', csv_export_2, name='csv-export-2'),
    path('report_3/', csv_export_3, name='csv-export-3'),
    path('marks-details',marks_details,name='marks-details'),
    path('suggested-list',suggested_list,name="suggested-list")
]
