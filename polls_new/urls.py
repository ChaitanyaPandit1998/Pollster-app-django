from django.urls import path

from . import views

app_name='polls_new'

urlpatterns=[
    path('',views.index,name='index'),
]


