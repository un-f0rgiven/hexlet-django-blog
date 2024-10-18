from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, tags, article_id):
        context = {'text': f'Статья номер {article_id}. Тег {tags}'}

        return render(request, 'articles/index.html', context=context)
