from django.urls import path
from .views import *


urlpatterns = [

    path('', PostList.as_view()),
    path('new/<int:pk>', DetailPost.as_view(), name='post'),
    path('news/create/', PostCreate.as_view(), name='create'),
    path('article/create/', ArticleCreate.as_view(), name='create'),
    path('news/search', PostSearch.as_view(), name='search'),
    path('new/<int:pk>/edit/', PostUpdate.as_view(), name='edit'),
    path('new/<int:pk>/delete/', PostDelete.as_view(), name='delete'),

]