# -*- coding: utf-8 -*-
from odoo import http

class CustomSalesPedroLara(http.Controller):

    @http.route('/app/', auth='public')
    def example(self, **kw):
        return http.request.render('custom_main_page_pedro_lara.example_page', {})
