from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from webapp.forms import AnswerForm
from webapp.models import Poll


class CreateAnswer(CreateView):
    form_class = AnswerForm
    template_name = 'answers/create.html'

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.poll.pk})