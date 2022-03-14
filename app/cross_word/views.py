from django.shortcuts import render, redirect
from .models import HorizonalHint, VerticalHint
# Create your views here
# クロスワード画面.
def index(request):
    params = {
        'vertical':[],
        'horizonal':[],
    }
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
        'ans': 'OSS(Open Source Software)',
        'comment':'OSS(Open Source Software)は,ソフトウェアのソースコードが一般に公開され、商用および非商用の目的を問わずソースコードの利用・修正・再頒布が可能なソフトウェアと定義される。オープンソースライセンスが課せられたソフトウェアやパブリックドメインに置かれたソースコードとそのソフトウェアなどがそれに当たる。',
        'vertical':[],
        'horizonal':[],
    }
    params['vertical']=VerticalHint.objects.filter(crossword_id=1)
    params['horizonal']=HorizonalHint.objects.filter(crossword_id=1)
    return render(request, 'cross_word/answer1.html', params)



# def index(request):
#     params = {
#         # 'select':QuizSelect(),
#         'form':AnswerForm(),
#     }
#     return render(request,'quiz/index.html',params)
