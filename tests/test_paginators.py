from django.core.paginator import Paginator

from paginator.paginators import paginate


def test_paginate():
    p = Paginator(range(15), 2)
    pg = paginate({'paginator': p, 'page_obj': p.page(1)})
    # TODO finish
