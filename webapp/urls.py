from django.urls import path

from webapp.views import *

urlpatterns = [
    path('', PollsView.as_view(), name='index'),
]
