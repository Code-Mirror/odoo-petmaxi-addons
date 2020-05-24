# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pedrolara_customResPartner(models.Model):
    _inherit = 'res.partner'
    sepa_code = fields.Char('Código de autorización SEPA')

class pedrolara_customAccountInvoice(models.Model):
    _inherit = 'account.invoice'    
    partner_sepa_code = fields.Char(related='partner_id.sepa_code', string='Código de autorización SEPA', readonly=True)
    


