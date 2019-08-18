from django import template

register = template.Library()


@register.filter()
def new_filter(value, v=""):
    return value + "sb" + v
