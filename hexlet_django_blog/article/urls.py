from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleFormView, ArticleFormCreateView, ArticleFormEditView


urlpatterns = [
    path('', IndexView.as_view(), name='articles_index'),
    path('<int:id>/', ArticleFormView.as_view(), name='article'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
]
