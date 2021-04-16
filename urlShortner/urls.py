from django.contrib import admin
from django.urls import path

from authentication.views import *
from urlhandler.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', login, name = "login"),
    path('signup/', signup, name = "signup"),
    path('logout/', logout, name = "logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('generate/', generate, name="generate"),
    path('<str:short>', home, name="home"),
]
