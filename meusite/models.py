from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
  titulo = models.CharField(max_length=255)
  conteudo = models.TextField()
  data_publicacao = models.DateTimeField(auto_now_add=True)
  autor = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return self.titulo
  
  
class Comment(models.Model):
  post = models.ForeignKey(Post, related_name='comentarios',on_delete=models.CASCADE)
  autor = models.ForeignKey(User, on_delete=models.CASCADE)
  conteudo = models.TextField()
  data_criacao = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'Comentario de {self.autor} on {self.post.titulo}'
    