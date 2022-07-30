from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import ChoiceForm
from webapp.models import Poll


class CreateChoice(CreateView):
    form_class = ChoiceForm
    template_name = 'choices/create.html'

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('poll', kwargs={'pk': self.object.poll.pk})
