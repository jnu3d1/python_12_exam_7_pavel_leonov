from django.urls import path

from webapp.views import *

urlpatterns = [
    path('', PollsView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll'),
    path('polls/add/', CreatePoll.as_view(), name='create_poll'),
    path('poll/<int:pk>/editing/', UpdatePoll.as_view(), name='edit_poll'),
    path('poll/<int:pk>/delete', DeletePoll.as_view(), name='delete_poll'),
    path('poll/<int:pk>/choices/add/', CreateChoice.as_view(), name='create_choice'),
]
