from django import template

register = template.Library()

@register.filter
def excitred(value):
    return f"{value}!!!"

