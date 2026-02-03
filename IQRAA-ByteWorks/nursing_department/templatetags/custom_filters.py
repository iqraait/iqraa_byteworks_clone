from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Return dictionary value by key in template"""
    if dictionary and key in dictionary:
        return dictionary.get(key)
    return None


from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, [])

