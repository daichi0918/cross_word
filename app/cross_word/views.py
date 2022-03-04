from django.shortcuts import render, redirect
# Create your views here
# クロスワード画面.
def index(request):
    if request.method == "POST":
        answer = 'oss'
        word = request.POST['word'].lower()
        if answer == word:
            return redirect('cross_word:answer1')
    return render(request, 'cross_word/cross_word.html')

def answer1(request):
    params = {
        'ans': 'OSS(Open Source Software)',
    }
    return render(request, 'cross_word/answer1.html', params)



# def index(request):
#     params = {
#         # 'select':QuizSelect(),
#         'form':AnswerForm(),
#     }
#     return render(request,'quiz/index.html',params)
