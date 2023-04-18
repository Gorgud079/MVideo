from django import template
from django.template.loader import render_to_string

from Menu.models import MenuItem
register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context):
    menu0 = MenuItem.objects.filter(level=0)
    context = {'menu0': menu0}

    return context

@register.simple_tag()
def draw_menu(context):
    menu0 = MenuItem.objects.filter(level=0)
    context = {'menu0': menu0}

    return context