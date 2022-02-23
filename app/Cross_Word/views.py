from django.shortcuts import render, redirect

# Create your views here
# クロスワード画面.
def index(request):
    if request.method == "POST":
        answer = 'データ'
        word = request.POST['word']
        if answer == word:
            return redirect('cross_word:answer1')
    return render(request, 'cross_word.html')

def answer1(request):
    return render(request, 'answer1.html')