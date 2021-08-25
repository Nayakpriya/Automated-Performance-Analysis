from django.contrib import admin
from student.models import Question,Marks
from  django.contrib.auth.models  import  Group  
# Register your models here.

admin.site.unregister(Group) 
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("topic", "question", "course_outcomes","test")
    list_filter = ("course_outcomes","test") 

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display=("student_name","usn","total","test")
    list_filter=("test",)
