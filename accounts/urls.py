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
    path('all_users/', views.UserListView.as_view(), name = 'all_users'),
    path('delete_user/<int:pk>', views.UserDeleteView.as_view(), name = 'delete_user'),
    path('delete_thread/<int:pk>', views.ThreadDeleteView.as_view(), name = 'delete_thread'),
    path('delete_singular/<int:pk>', views.SingularDeleteView.as_view(), name = 'delete_singular'),
    path('create_cards', views.createcards, name = 'create_cards'),

]