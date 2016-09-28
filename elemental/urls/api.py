from django.conf.urls import include, url
from django.http import HttpResponse
from rest_framework import routers

from elemental.views import MenuViewSet

router = routers.DefaultRouter()
router.register(r'menus', MenuViewSet)


def page_view(request, slug):
    return HttpResponse(slug)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
