from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework import status
from .models import Post


def posts(request):
  posts = Post.objects.order_by('data-public')
  return render(request, 'base.html', {'posts':posts})

def post_detalhes(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detalhes.html', {'post': post})
  
def minha_view(request):
  return render(request, 'templates/base.html')  
  
class MyApiView(APIView):
    def get(self, request):
        try:
            # Recuperar todos os posts do banco de dados
            posts = Post.objects.all()
            
            # Serializar os dados
            serializer = PostSerializer(posts, many=True)
            
            # Retornar os dados serializados como uma resposta JSON
            return Response(serializer.data)
        except Exception as e:
            # Em caso de exceção, retornar uma resposta de erro com status 400
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)