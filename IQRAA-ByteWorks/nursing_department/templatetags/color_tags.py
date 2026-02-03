# nursing_department/templatetags/color_tags.py
from django import template

register = template.Library()

@register.filter
def color_for_percentage(value):
    """Return Tailwind text color class based on percentage value."""
    try:
        val = float(value)
    except (ValueError, TypeError):
        return "text-gray-600"

    if val < 65:
        return "text-red-600"
    elif val < 75:
        return "text-orange-500"
    elif val < 90:
        return "text-green-600"
    else:
        return "text-blue-600"
