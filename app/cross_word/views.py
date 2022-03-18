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

# OSS
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
        objects = Cross_wordSomething.objects.filter(crossword_id=1)
        for object in objects:
            answer = object.crossword_ans
            word = request.POST['word'].upper()
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

# SSD
def easy2(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'mistake': '',
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=4)
    params['vertical']=VerticalHint.objects.filter(crossword_id=4)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=4)
    if request.method == "POST":
        objects = Cross_wordSomething.objects.filter(crossword_id=4)
        for object in objects:
            answer = object.crossword_ans
            word = request.POST['word'].upper()
            if answer == word:
                return redirect('cross_word:easy_answer2')
            else:
                params['mistake']=random.choice(n)
    return render(request, 'cross_word/easy2.html', params)

def easy_answer2(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'explanation':[],
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=4)
    params['vertical']=VerticalHint.objects.filter(crossword_id=4)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=4)
    params['explanation']=random.choice(l)
    return render(request, 'cross_word/easy_answer2.html', params)

# データ
def nomal(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'mistake': '',
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=2)
    params['vertical']=VerticalHint.objects.filter(crossword_id=2)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=2)
    if request.method == "POST":
        objects = Cross_wordSomething.objects.filter(crossword_id=2)
        for object in objects:
            answer = object.crossword_ans
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
    params['something']=Cross_wordSomething.objects.filter(crossword_id=2)
    params['vertical']=VerticalHint.objects.filter(crossword_id=2)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=2)
    params['explanation']=random.choice(l)
    return render(request, 'cross_word/nomal_answer.html', params)

# APT
def nomal2(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'mistake': '',
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=5)
    params['vertical']=VerticalHint.objects.filter(crossword_id=5)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=5)
    if request.method == "POST":
        objects = Cross_wordSomething.objects.filter(crossword_id=5)
        for object in objects:
            answer = object.crossword_ans
            word = request.POST['word'].upper()
            if word in answer:
                return redirect('cross_word:nomal_answer2')
            else:
                params['mistake']=random.choice(n)
    return render(request, 'cross_word/nomal2.html', params)

def nomal_answer2(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'explanation':[],
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=5)
    params['vertical']=VerticalHint.objects.filter(crossword_id=5)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=5)
    params['explanation']=random.choice(l)
    return render(request, 'cross_word/nomal_answer2.html', params)


# こあら'こあら', 'コアラ', '子守熊', '袋熊']
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
        objects = Cross_wordSomething.objects.filter(crossword_id=3)
        for object in objects:
            answer = object.crossword_ans
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


# PERFECT
def hard2(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'mistake': '',
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=6)
    params['vertical']=VerticalHint.objects.filter(crossword_id=6)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=6)
    if request.method == "POST":
        objects = Cross_wordSomething.objects.filter(crossword_id=6)
        for object in objects:
            answer = object.crossword_ans
            word = request.POST['word']
            if word in answer:
                return redirect('cross_word:hard_answer2')
            else:
                params['mistake']=random.choice(n)
    return render(request, 'cross_word/hard2.html', params)

def hard_answer2(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
        'explanation':[],
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=6)
    params['vertical']=VerticalHint.objects.filter(crossword_id=6)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=6)
    params['explanation']=random.choice(l)
    return render(request, 'cross_word/hard_answer2.html', params)



