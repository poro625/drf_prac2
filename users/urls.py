
from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,    
)
from users import views


urlpatterns = [
    path('signup/', views.UserVeiw.as_view() ,name='user_view'),
    path('mock/', views.MockView.as_view() ,name='mock_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('follow/<int:user_id>/', views.FollowView.as_view(), name='follow_view'),
    
]