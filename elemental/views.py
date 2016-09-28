from django.views.generic.detail import DetailView
from rest_framework import viewsets

from .models import Menu, Page
from .serializers import MenuSerializer


class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class PageDetailView(DetailView):
    model = Page
    context_object_name = "page"
