from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from level.models import QuestionAll
# from app.models import User # モデルをインポート

# Create your views here.
def index(request):
    return HttpResponse("Levelページ")

def select(request):
    # return render(request, 'select.html')
    return render(request, 'level/select.html')

def easy(request):
    # return render(request, 'easy.html')
    return render(request, 'level/easy.html')

def nomal(request):
    # return render(request, 'nomal.html')
    return render(request, 'level/nomal.html')

def hard(request):
    # return render(request, 'hard.html')
    return render(request, 'level/hard.html')

# def users(request):
#     user_list = User.objects.all() # 値一覧を取得
#     user_dict = {'users': user_list} # ディクショナリーの形で設定

#     return render(request, 'app/users.html', context=user_dict) # context=user_dictとして、users.htmlに渡す

def list(request):
    question_list = QuestionAll.objects.all()
    # list_dict = {'question': list1}
    return render(request, 'level/easy.html', {'question':question_list})