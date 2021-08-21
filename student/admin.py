from django.contrib import admin
from student.models import Question,Marks
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("topic", "question", "course_outcomes","test")
    list_filter = ("course_outcomes",) 

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display=("student_name","usn","total")
    list_filter=("test",)
