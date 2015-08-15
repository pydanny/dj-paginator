from django.test import TestCase

from django.core.paginator import Paginator

from paginator.paginators import paginate


class PaginatorTestCase(TestCase):

    def test_paginate(self):
        paginator = Paginator(list(range(15)), 2)
        self.assertEqual(paginator.num_pages, 8)
        # pg = paginate({'paginator': paginator,
        #   'page_obj': paginator.page(1)})
