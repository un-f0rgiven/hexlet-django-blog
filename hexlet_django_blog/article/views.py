from django.shortcuts import render


def index(request):
    name = 'Article (context)'
    description = 'Овладеваю Django'
    joke = 'Django! Django!! Django!!!'
    return render(request, 'articles/index.html', context={'name': name, 'description': description, 'joke': joke})
