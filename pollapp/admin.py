from django.contrib import admin
from .models import Question,choice

class choiceinline(admin.TabularInline):
    '''
        TabularInline声明以表格的形式显示内嵌关联对象
    '''
    model = choice
    extra = 3

class Questionadmin(admin.ModelAdmin):
    '''
        choice 对象在question 管理界面中编辑
        告诉django 默认提供三个choice空间
    '''
    fieldsets = [
        (None,              {'fields':['question_text']}),     #字段集的形式  前面是字段名称
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [choiceinline]

    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']  #admin 页面右侧将会显示一个filter 模块
    search_fields = ['question_text']   #添加的搜索功能  一个搜索框


admin.site.register(Question,Questionadmin)
# admin.site.register(choice)
