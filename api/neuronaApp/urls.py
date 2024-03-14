from django.urls import path, include
from rest_framework.routers import DefaultRouter

from neuronaApp import views

router = DefaultRouter()
router.register(r'validity', views.Validity, basename='validity')
router.register(r'passkey-options', views.PasskeyChallengeView, basename='passkey-options')

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]
