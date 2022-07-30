from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from webapp.models import Poll


class PollsView(ListView):
    model = Poll
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    ordering = ('-created_at')
    paginate_by = 5


class PollView(DetailView):
    model = Poll
    template_name = 'polls/poll.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choises'] = self.object.choices.all()
        return context