from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']

    def clean_question(self):
        question = self.cleaned_data.get('question')
        if len(question) > 50:
            raise ValidationError('Вопрос не должен превышать 50 символов!')
        return question
