from django.urls import path, include

from . import views

from .models import Article, Reporter
from rest_framework import routers, serializers, viewsets


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ReporterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reporter
        fields = ['full_name']


class ReporterViewSet(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'reporter', ReporterViewSet)


urlpatterns = [
    path('', views.index, name='index'),

    path('<int:article_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:article_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:article_id>/vote/', views.vote, name='vote'),

    path('api/', include(router.urls))
]
