from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('signup/', views.SignupView.as_view(), name='signup' ),
    path('profile/', views.UpdateProfile.as_view(), name='profile'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]