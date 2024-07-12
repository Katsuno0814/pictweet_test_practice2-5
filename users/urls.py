from django.urls import path

from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = "users"
urlpatterns = [
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign_in/', LoginView.as_view(template_name='users/sign_in.html'), name='sign_in'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('<int:pk>/', views.UserPageView.as_view(), name='mypage'),
]