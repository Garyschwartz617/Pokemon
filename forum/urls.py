from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('thread/', views.CreateThreadView.as_view(), name = 'thread'),
    path('comment/<int:pk>', views.CreateCommentView.as_view(), name = 'comment'),


]