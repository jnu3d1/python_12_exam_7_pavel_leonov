from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from webapp.models import Poll


class PollsView(ListView):
    model = Poll
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    ordering = ('-created_at')