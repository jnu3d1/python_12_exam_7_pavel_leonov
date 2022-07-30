from django.db import models


# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=50, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания опроса')

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    text = models.CharField(max_length=50, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='choices', verbose_name='Опрос')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'choices'
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
