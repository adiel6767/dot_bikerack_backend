from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

# Define your URL patterns
urlpatterns = [
    # Add other custom endpoints
    path('data/<str:Site_ID>/', views.BikeRackDataDetail.as_view(), name='data-detail'),  
    path('data/create/', views.BikeRackDataCreate.as_view(), name='data-create'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('user/', views.UserView.as_view(), name='user'),
    path('achievements/',views.AchievementsView.as_view(), name='achievements'),
    path('badge/',views.BadgeView.as_view(), name='badge'),
    path('leaderboard/', views.LeaderboardListView.as_view(), name='leaderboard'),

] 

