from django.conf.urls import url
from django.http import HttpResponse


def page_view(request, slug):
    return HttpResponse(slug)

urlpatterns = [
    url(r"^(?P<slug>[\w-]+)$", page_view, name="page")
]
