from django.conf import settings
from django import template

from paginator.paginators import paginate

register = template.Library()

PAGINATOR_THEME = getattr(settings, "PAGINATOR_THEME", "bootstrap")

theme = 'paginator/{}/paginator.html'.format(PAGINATOR_THEME)


@register.inclusion_tag('paginator/bootstrap/paginator.html', takes_context=True)
def bootstrap_paginator(context):
    return paginate(context)

@register.inclusion_tag(theme, takes_context=True)
def paginator(context):
    return paginate(context)
