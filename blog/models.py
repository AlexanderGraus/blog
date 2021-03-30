from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #funcion que vamos a usar cuando queramos publicar un post ya creado
    def publish(self): 
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment = True)

class Comment(models.Model):
    # le estoy indicando que cada comentario va a tener un post
    # con related_name me permite acceder al comentario desde el modelo Post
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
