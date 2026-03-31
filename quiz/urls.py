from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('quiz/<slug:slug>/', views.QuizDetailView.as_view(), name='quiz_detail'),
    path('quiz/<slug:slug>/take/', views.QuizTakingView.as_view(), name='quiz_take'),
    path('history/', views.UserHistoryView.as_view(), name='user_history'),
    path('history/<int:pk>/', views.attempt_detail, name='attempt_detail'),
    path('quiz/<slug:slug>/result/', views.ResultView.as_view(), name='quiz_result'),
]
