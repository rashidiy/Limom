# shop/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def round_value(value):
    """Round the value to the nearest integer."""
    try:
        return round(value)
    except (TypeError, ValueError):
        return value


@register.filter
def range_filter(value):
    """Generate a range of values up to the given number."""
    try:
        return range(1, int(value) + 1)  # range starts from 1 to value
    except (TypeError, ValueError):
        return []