from django.urls import path, include
from rest_framework.routers import DefaultRouter
from meusite.views import posts, post_detalhes
from .api import PostViewSet, CommentViewSet
from .views import minha_view

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', posts, name='posts'),
    path('post/<int:post_id>/', post_detalhes, name='post_detalhes'),
    path('api/', include(router.urls)),
    path('minha-rota/', minha_view, name='minha_view'),
]