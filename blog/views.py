from django.shortcuts import render
from django.utils import timezone
from .models import Post
#подключение модели с models.py
#подключение модели и шаблона html, также сортировка постов по дате публикации
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    #{}, — это место, куда мы можем добавить что-нибудь для использования в шаблоне