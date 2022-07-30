from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']

    def clean_question(self):
        question = self.cleaned_data.get('question')
        if len(question) > 50:
            raise ValidationError('Вопрос не должен превышать 50 символов!')
        return question


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) > 50:
            raise ValidationError('Вариант ответа не должен превышать 50 символов!')
        return text


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['choices']
        widgets = {
            'choices': widgets.CheckboxInput
        }
