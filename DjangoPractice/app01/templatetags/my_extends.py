from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name="my_static")
def static_path(value):
    static = settings.STATIC_URL
    return static + value


@register.inclusion_tag(filename="inclusion_tag_tmp.html", name="inclusion")
def inclusion_fun(num):
    data = [x for x in range(1, num+1)]
    return {"data": data}

