from django.shortcuts import render, redirect
from .models import HorizonalHint, VerticalHint, Cross_wordSomething
# Create your views here
# クロスワード画面.
def index(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=1)
    params['vertical']=VerticalHint.objects.filter(crossword_id=1)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=1)
    if request.method == "POST":
        answer = 'oss'
        word = request.POST['word'].lower()
        if answer == word:
            return redirect('cross_word:answer1')
    return render(request, 'cross_word/cross_word.html', params)

def answer1(request):
    params = {
        'something':[],
        'vertical':[],
        'horizonal':[],
    }
    params['something']=Cross_wordSomething.objects.filter(crossword_id=1)
    params['vertical']=VerticalHint.objects.filter(crossword_id=1)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=1)
    return render(request, 'cross_word/answer1.html', params)



