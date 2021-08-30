from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # path('', views.cards, name = 'card'),
    path('', views.CardListView.as_view(), name = 'card'),
    path('my_cards/', views.MyCardListView.as_view(), name = 'my_cards'),
    path('post/<int:pk>', views.CreatePostView.as_view(), name = 'post'),
    path('all_posts/', views.PostListView.as_view(), name = 'all_posts'),
    path('response/<int:pk>', views.CreateResponseView.as_view(), name = 'response'),
    path('responses/<int:pk>',views.PostdetailView.as_view(), name = 'all_response'),
    path('answer/<int:pk>', views.CreateAnswerView.as_view(), name = 'answer'),

]