# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pedrolara_partnerFieldsPaymentMethod(models.Model):
    _inherit = 'res.partner'
    comment_payment_method = fields.Text('Notas para mostrar en las facturas')
    comment_sale_order = fields.Text('Notas para mostrar en las ventas')

class pedrolara_invoiceFieldsPaymentMethod(models.Model):
    _inherit = 'account.invoice'    
    invoice_comment_payment_method = fields.Text(related='partner_id.comment_payment_method', string='Notas para mostrar en las facturas', readonly=True)

class pedrolara_customOrderFieldsComment(models.Model):
    _inherit = 'sale.order'    
    order_comment = fields.Text(related='partner_id.comment_sale_order', string='Notas para mostrar en las ventas', readonly=True)
    


