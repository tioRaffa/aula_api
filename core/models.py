from django.db import models

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
class Course(Base):
    title = models.CharField(("Titulo"), max_length=250)
    url = models.URLField(unique=True)
    
    
    def __str__(self):
        return self.title
    
class Evaluation(Base):
    course = models.ForeignKey(Course, verbose_name=("Curso"), on_delete=models.CASCADE)
    name = models.CharField(("Nome"), max_length=150)
    email = models.EmailField(("Email"), max_length=254)
    comment = models.TextField(("Comentario"), blank=True, default='')
    evaluation = models.DecimalField(("Avaliação"), max_digits=2, decimal_places=1)
    
    class Meta:
        unique_together = [
            'email',
            'course',
        ]
    
    
    def __str__(self):
        return f'{self.name} avaliou com nota ({self.evaluation}) o curso: {self.course}'