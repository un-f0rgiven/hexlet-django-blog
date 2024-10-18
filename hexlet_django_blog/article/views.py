from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        name = 'Article'

        return render(request, 'articles/index.html', context={'name': name})
