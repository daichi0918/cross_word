from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import QuestionAll, Friend

# Create your views here.
def index(request):
    return HttpResponse("Levelページ")

def select(request):
    # return render(request, 'select.html')
    return render(request, 'level/select.html')

def easy(request):
    # return render(request, 'easy.html')
    params = {
        'friend': [],
    }
    params['friend']=Friend.objects.all()
    questionModel = {'question': QuestionAll.objects.all()}
    return render(request, 'level/easy.html', params)

def nomal(request):
    # return render(request, 'nomal.html')
    return render(request, 'level/nomal.html')

def hard(request):
    # return render(request, 'hard.html')
    return render(request, 'level/hard.html')

# def list(request):
#     # question_list = QuestionAll.objects.all()

#     params = {
#         'friend': [],
#     }
#     params['friend']=Friend.objects.all()
#     questionModel = {'question': QuestionAll.objects.all()}
#     return render(request, 'level/easy.html', params)

