from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='еда'
    )
    ingredients = models.TextField(
        verbose_name='ингредиенты'
    )
    instructions  = models.TextField(
        verbose_name='инструкция по готовке'
    )
    prep_time = models.IntegerField(
        verbose_name='время готовки'
    )
    is_vegetarian = models.BooleanField(
        default=False,
        verbose_name='еда вегетареанское'
    )
    created_at  = models.DateTimeField(
        auto_now_add = True,
        verbose_name='день дегустации'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'вкусная кухня😋'

