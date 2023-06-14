from django.urls import include, path 
from . import views




#URLConf
urlpatterns = [
    path('',views.home_page, name='homepage')
    ]