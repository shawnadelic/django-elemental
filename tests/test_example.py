import pytest

from elemental.models import Menu, Link, Page
from elemental.utils import get_menu_by_identifier


@pytest.mark.django_db
def test_get_menu_by_identifier():
    assert get_menu_by_identifier("homebase") is None

    page = Page.objects.create(title="Home", slug="home", ordering=1)
    link = Link.objects.create(title="Projects", url="projects", ordering=0)
    menu = Menu.objects.create(title="Main", identifier="main")
    menu.pages.add(page)
    menu.links.add(link)
    assert get_menu_by_identifier("main") == menu

    assert menu.items[0]["url"] == link.get_url()
    assert menu.items[1]["url"] == page.get_url()

    link.ordering = 2
    link.save()
    assert menu.items[0]["url"] == page.get_url()
    assert menu.items[1]["url"] == link.get_url()
