from django.conf.urls import url

from elemental.views import PageDetailView

urlpatterns = [
    url(r"^(?P<slug>[\w-]+)$", PageDetailView.as_view(), name="page"),
]
