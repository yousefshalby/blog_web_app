from django.urls import path, include
from rest_framework import routers
from users import api
from .api import viewsets_profile, fbv_user_list, fbv_user_pk
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register("user", viewsets_profile)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('tokenrequest/', obtain_auth_token),
    path('rest/fbv/', api.fbv_user_list),
    path('rest/fbv/<int:pk>', api.fbv_user_pk),
    path ('', include(router.urls)),


]