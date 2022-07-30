from django.db import models


# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=50, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания опроса')
    choices = models.ManyToManyField('webapp.Choice', related_name='polls', through='webapp.Answer',
                                     through_fields=('poll', 'choice'))

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    text = models.CharField(max_length=50, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='ch0ices', verbose_name='Опрос')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'choices'
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='ch0ice', verbose_name='Опрос')
    choice = models.ForeignKey('webapp.Choice', on_delete=models.CASCADE, related_name='p0ll',
                               verbose_name='Вариант ответа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата прохождения опроса')
