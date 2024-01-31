from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .models import NewsTest, Like
from .forms import NewsTestForm
# Create your views here.

# sepehr : 1234
# admin1 : sepehr11
# admin2 : sepehr22

def show_news(request):
    news = NewsTest.objects.select_related().all()
    news = list(news)
    m = {}
    for new in news:
        m[new] = f'{new.likes.count()}'


    return render(request, 'home.html', {'news': m, 'user': request.user})

def show_news_detail(request, pk):
    news = NewsTest.objects.get(id=pk)
    likes = news.likes.count()
    # user_like = news.likes.user
    user_like = Like.objects.filter(item = news)

    return render(request, 'news_detail.html', {'news': news, 'likes': likes, 'user_like': user_like})

def like_news(request, pk):
    news = NewsTest.objects.get(id=pk)

    exited_like = Like.objects.filter(user=request.user, item=news).exists()
    
    if exited_like == False:
        Like.objects.create(user=request.user, item=news)

    # return render(request, 'home.html')#, pk=news.pk)
    return redirect('news')

def create_news(request):
    if request.method == 'POST':
        form = NewsTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsTestForm()

    return render(request, 'create.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('news')