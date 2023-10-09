from django.db import models
from authentication.models import MyUser

# Create your models here.


class Blog(models.Model):
    title = models.CharField("Titulo del blog", max_length=50, unique=True)
    description = models.CharField("Descripcion del blog", max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    
