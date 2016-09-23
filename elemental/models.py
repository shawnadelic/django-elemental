from django.db import models
from django.utils.encoding import force_text
from django.urls import reverse
from ckeditor.fields import RichTextField


class Menu(models.Model):
    title = models.CharField(max_length=120)
    identifier = models.CharField(max_length=120)
    pages = models.ManyToManyField("Page")
    links = models.ManyToManyField("Link")

    @property
    def items(self):
        pages = list(self.pages.all())
        links = list(self.links.all())
        items = [
            {
                "ordering": item.ordering,
                "title": item.title,
                "url": item.get_url()
            } for item in (pages + links)
        ]
        return sorted(items, key=lambda item: item["ordering"])

    def __str__(self):
        return force_text(self.title)


class MenuItem(models.Model):
    title = models.CharField(max_length=120)
    visible_to_public = models.BooleanField(default=False)
    visible_in_menus = models.BooleanField(default=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return force_text(self.title)


class Link(MenuItem):
    url = models.URLField(max_length=50)

    def get_url(self):
        try:
            url = reverse(self.url)
        except Exception:
            url = self.url
        return url


class Page(MenuItem):
    slug = models.SlugField(max_length=50)
    body = RichTextField(blank=True, null=True)

    def get_url(self):
        return "/%s" % self.slug
