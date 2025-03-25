from django.urls import path, include
from rest_framework import routers

from api.views import api_auth, api_location, api_survey

router = routers.DefaultRouter()

# USERS
router.register("users", api_auth.UserViewSet, basename="users")
router.register("profiles", api_auth.ProfileViewSet, basename="profiles")

# LOCATION
router.register("desa", api_location.DesaViewSet, basename="desa")
router.register("kecamatan", api_location.KecamatanViewSet, basename="kecamatan")
router.register("kabupaten", api_location.KabupatenViewSet, basename="kabupaten")
router.register("provinsi", api_location.ProvinsiViewSet, basename="provinsi")

# SURVEY
router.register("survey", api_survey.SurveyViewSet, basename="survey")
router.register("respondent", api_survey.RespondentViewSet, basename="respondent")

from django.views.generic import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", RedirectView.as_view(url="/api/v1/"), name="api-root"),
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/', api_auth.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/register/', api_auth.RegisterView.as_view({"post": "create"}), name='register'),
    path("api/v1/", include(router.urls)),
]

# handler502 = 'core.views.custom_error_502'

