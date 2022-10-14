from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.home, name="home"),
   path('blank_board', views.blank_board, name="blank_board"),
   path('sc', views.sc, name="sc"),
]