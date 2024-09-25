from django.urls import path
from . views import *

urlpatterns = [
    path('thoughts/',  ThoughtsApiView.as_view()  ),
    path('thoughts/<int:pk>/', GetSpecificThought.as_view() ),
]