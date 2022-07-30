from django.urls import path

from webapp.views import *

urlpatterns = [
    path('', PollsView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll'),
]
