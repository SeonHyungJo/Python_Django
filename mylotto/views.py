from django.shortcuts import render
from .models import GuessNumbers
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos': lottos})


def post(request):
    #post방식으로 받았을때 처리
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('lotto:index')
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form' : form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, 'lotto/detail.html', {'lotto': lotto})
