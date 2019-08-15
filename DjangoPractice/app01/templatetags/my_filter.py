from django import template

register = template.Library()


@register.filter()
def new_filter(value):
    return value + "sb"
