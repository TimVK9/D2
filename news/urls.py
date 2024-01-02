from django.urls import path
from .views import *

urlpatterns = [

    path('', PostList.as_view()),
    path('new/<int:pk>', DetailPost.as_view(), name='post')


]