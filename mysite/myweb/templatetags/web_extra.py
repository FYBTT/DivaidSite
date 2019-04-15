from django import template

register = template.Library()

@register.filter(name='hash')
def hash(map, item):
    return map[item]