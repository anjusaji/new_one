from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html')),
    path('login/', views.Login.as_view(), name='login'),
	path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('home/',views.Home.as_view()),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('register/', views.Register.as_view(), name='user_register'),
]
