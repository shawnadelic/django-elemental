from .models import Menu


def get_menu_by_identifier(identifier):
    return Menu.objects.filter(identifier=identifier).first()
