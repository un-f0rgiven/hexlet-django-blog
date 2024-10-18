from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView, View

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Geralt'

        return context


class HomePageView(View):
    def get(self, request):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))

def about(request):
    return render(request, 'about.html')