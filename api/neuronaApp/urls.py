from django.urls import path, include
from rest_framework.routers import DefaultRouter

from neuronaApp import views
from neuronaApp.views import PostsViewSet, CommentsViewSet

router = DefaultRouter()
router.register(r'validity', views.Validity, basename='validity')
router.register(r'passkey-options', views.PasskeyChallengeView, basename='passkey-options')
router.register(r'posts', PostsViewSet)
router.register(r'comments', CommentsViewSet, basename='comments')
router.register(r'profile', views.Profile, basename='profile')

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("", include(router.urls)),
    path('spaces/', views.space_view.get_spaces, name='get_spaces'),
    path('spaces/<int:pk>/', views.space_view.get_space, name='get_space'),
    path('spaces/', views.space_view.create_space, name='create_space'),
    path('spaces/<int:pk>/', views.space_view.update_space, name='update_space'),
    path('spaces/<int:pk>/', views.space_view.delete_space, name='delete_space'),
    path('posts/<int:pk>/upvote/', views.VoteView.as_view(actions={'post': 'upvote'}), name='upvote'),
    path('posts/<int:pk>/downvote/', views.VoteView.as_view(actions={'post': 'downvote'}), name='downvote'),
    path('posts/<int:pk>/unvote/', views.VoteView.as_view(actions={'post': 'unvote'}), name='unvote'),
]
