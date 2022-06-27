from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=40)
    release_date = models.DateField()
    director_name = models.CharField(max_length=40)
    description = models.TextField(blank= True, null=True)

    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    post = models.ForeignKey(Movies,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comentario: {self.body} \n comentado por: {self.name}'