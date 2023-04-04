from django import template
from Menu.models import MenuItem
register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context):
    menu0 = MenuItem.objects.filter(level=0)
    return {
        'menu0': menu0,
    }