from django.shortcuts import render, redirect
import random
from .models import HorizonalHint, VerticalHint, Cross_wordSomething
# Create your views here
# クロスワード画面.

# 正解時のメッセージ
l = ['----- 正解です！ -----',
        '----- おめでとう！ -----',
        '----- very good!!! -----', 
        '----- more play!!! -----', 
        '----- おはようございます-----',
        'Created by E-TEAM'
        ]

n = ['----- ざんねん！ -----',
        '----- おしい！ -----',
        '----- one more play!!! -----', 
        '----- 再チャレンジ!!! -----', 
        '----- I have a dream today! -----',
        'Created by E-TEAM'
        ]

def easy(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'mistake': '',
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=1)
    params['vertical']=VerticalHint.objects.filter(crossword_id=1)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=1)
    if request.method == "POST":
        answer = 'oss'
        word = request.POST['word'].lower()
        if answer == word:
            return redirect('cross_word:easy_answer')
        else:
            params['mistake']=random.choice(n)
    return render(request, 'cross_word/easy.html', params)

def easy_answer(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'explanation':[],
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=1)
    params['vertical']=VerticalHint.objects.filter(crossword_id=1)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=1)
    params['explanation']=random.choice(l)
    return render(request, 'cross_word/easy_answer.html', params)


def nomal(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'mistake': '',
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=1)
    params['vertical']=VerticalHint.objects.filter(crossword_id=1)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=1)
    if request.method == "POST":
        answer = ['ルート', 'るーと']
        word = request.POST['word']
        if word in answer:
            return redirect('cross_word:nomal_answer')
        else:
            params['mistake']=random.choice(n)
    return render(request, 'cross_word/nomal.html', params)

def nomal_answer(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'explanation':[],
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=1)
    params['vertical']=VerticalHint.objects.filter(crossword_id=1)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=1)
    params['explanation']=random.choice(l)
    return render(request, 'cross_word/nomal_answer.html', params)


def hard(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'mistake': '',
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=3)
    params['vertical']=VerticalHint.objects.filter(crossword_id=3)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=3)
    if request.method == "POST":
        answer = ['こあら', 'コアラ', '子守熊', '袋熊']
        word = request.POST['word']
        if word in answer:
            return redirect('cross_word:hard_answer')
        else:
            params['mistake']=random.choice(n)
    return render(request, 'cross_word/hard.html', params)

def hard_answer(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'explanation':[],
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=3)
    params['vertical']=VerticalHint.objects.filter(crossword_id=3)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=3)
    params['explanation']=random.choice(l)
    return render(request, 'cross_word/hard_answer.html', params)




