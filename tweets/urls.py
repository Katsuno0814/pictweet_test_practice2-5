from django.urls import path,include
from . import views
from .views import IndexView,CreateView,DeleteView,UpdateView,DetailView

app_name = 'Tweets'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tweets/create/', CreateView.as_view(), name='create'),
    path('tweets/<int:pk>/delete', DeleteView.as_view(), name='delete'),
    path('tweets/<int:pk>/update', UpdateView.as_view(), name='update'),
    path('tweets/<int:pk>/', DetailView.as_view(), name='detail'),
    path('tweets/<int:pk>/comments/', include('comments.urls')),
    path('tweets/search_tweets/', views.tweet_search, name='search'),
]