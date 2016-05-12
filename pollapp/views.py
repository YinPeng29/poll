#-*-coding:utf-8-*-

from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from .models import Question,choice
from django.core.urlresolvers import reverse

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'index.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    print (question)
    return render(request,'detail.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Question)
    response = 'you are looking at the results of question %s'
    return HttpResponse(response%question_id)

def vote(request,question_id):
    '''
        request.POST['choice'] 以字符串形式返回选择的Choice的ID
        如果在POST数据中没有提供choice，request.POST['choice']将引发一个KeyError。
        上面的代码检查KeyError，如果没有给出choice将重新显示Question表单和一个错误信息。
    '''
    p = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError,choice.DoesNotExist):
        return render(request,'detail.html',{
            'question':p,
            'error_message':'you didn\'t select a choice.',
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        #reverse()反向解析 url 'pollapps:results' 找到对应的url地址args传递id形成最终的地址
        return HttpResponseRedirect(reverse('pollapps:results',args=(p.id,)))

