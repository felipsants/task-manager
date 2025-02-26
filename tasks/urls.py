from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, TaskViewSet, verify_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Criando o router para o TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token/', verify_token, name='verify-token'),
    # Inclui todas as rotas do ViewSet automaticamente
    path('', include(router.urls)),
]
