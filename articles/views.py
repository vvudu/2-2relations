from django.shortcuts import render
from articles.models import Article

def articles_list(request):
    template = 'articles/news.html'
    
    # Извлекаем статьи из базы данных, сортируя по дате публикации
    articles = Article.objects.all().order_by('-published_at')
    

    context = {
        'articles': articles  # Передаем статьи в контекст
    }

    return render(request, template, context)
