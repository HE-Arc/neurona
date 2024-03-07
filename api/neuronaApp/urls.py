from rest_framework.routers import DefaultRouter

from neuronaApp import views

router = DefaultRouter()
router.register(r"challenge", views.PasskeyChallengeView, basename="challenge")

urlpatterns = router.urls
