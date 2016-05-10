from django.contrib import admin
from .models import Question,choice

class Questionadmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['question_text']}),     #字段集的形式  前面是字段名称
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]


admin.site.register(Question,Questionadmin)
# admin.site.register(choice)
