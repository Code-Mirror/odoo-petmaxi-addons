# -*- coding: utf-8 -*-
from odoo import http

# class CustomSalesPedroLara(http.Controller):
#     @http.route('/custom_sales_pedro_lara/custom_sales_pedro_lara/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_sales_pedro_lara/custom_sales_pedro_lara/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_sales_pedro_lara.listing', {
#             'root': '/custom_sales_pedro_lara/custom_sales_pedro_lara',
#             'objects': http.request.env['custom_sales_pedro_lara.custom_sales_pedro_lara'].search([]),
#         })

#     @http.route('/custom_sales_pedro_lara/custom_sales_pedro_lara/objects/<model("custom_sales_pedro_lara.custom_sales_pedro_lara"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_sales_pedro_lara.object', {
#             'object': obj
#         })