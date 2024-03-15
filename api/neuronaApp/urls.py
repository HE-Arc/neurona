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
    path('spaces/', space_view.get_spaces, name='get_spaces'),
    path('spaces/<int:pk>/', space_view.get_space, name='get_space'),
    path('spaces/create', space_view.create_space, name='create_space'),
    path('spaces/update/<int:pk>', space_view.update_space, name='update_space'),
    path('spaces/delete/<int:pk>', space_view.delete_space, name='delete_space'),
    path('spaces/post', space_view.create_space, name='create_space'),
]
