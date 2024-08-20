# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SignUpView

# URL routing for the ViewSet
router = DefaultRouter()
router.register(r'DemoApp', UserViewSet)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'), 
    path('', include(router.urls)), 
]
