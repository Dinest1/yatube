from django import template


register = template.Library()


menu = [
    {'title': 'Главная'}
]


@register.simple_tag()
def show_menu():
    return menu
