from django.db import models

# Create your models here.


class Task(models.Model):

    class PriorityChoise(models.TextChoices):
        Baixa = 'Baixa'
        Media = 'Média'
        Alta = 'Alta'

    def __str__(self):
        return f'{self.title}'

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    completed = models.BooleanField()
    priority = models.CharField(
        max_length=10,
        choices=PriorityChoise.choices,
        default=PriorityChoise.Baixa
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
