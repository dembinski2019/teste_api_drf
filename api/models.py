from django.db import models

class Category(models.Model):
    name = models.CharField('Nome',max_length=255)
    description = models.TextField('Descrição')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name