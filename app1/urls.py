from django.urls import path
from . views import *


urlpatterns = [
    path("",  home , name="homepage" ),
    # path("add/",  add ),
    path("add/", UserView.as_view() )
]