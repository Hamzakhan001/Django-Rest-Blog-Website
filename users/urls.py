from django.urls import path,include
from .views import UserAPIView,MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
	path('',UserAPIView.as_view()),
	path('login/',MyTokenObtainPairView.as_view()),
	path('token/refresh',TokenRefreshView.as_view())
]
