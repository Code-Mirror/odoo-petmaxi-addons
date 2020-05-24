# -*- coding: utf-8 -*-
from odoo import http

# class Pedro-lara-custom-delivery-slip(http.Controller):
#     @http.route('/pedro-lara-custom-delivery-slip/pedro-lara-custom-delivery-slip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pedro-lara-custom-delivery-slip/pedro-lara-custom-delivery-slip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pedro-lara-custom-delivery-slip.listing', {
#             'root': '/pedro-lara-custom-delivery-slip/pedro-lara-custom-delivery-slip',
#             'objects': http.request.env['pedro-lara-custom-delivery-slip.pedro-lara-custom-delivery-slip'].search([]),
#         })

#     @http.route('/pedro-lara-custom-delivery-slip/pedro-lara-custom-delivery-slip/objects/<model("pedro-lara-custom-delivery-slip.pedro-lara-custom-delivery-slip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pedro-lara-custom-delivery-slip.object', {
#             'object': obj
#         })