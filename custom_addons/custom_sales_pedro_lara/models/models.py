# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools import pycompat

"""
This Class inherit ProductProduct from sales module to add a new
attribute << udPallet >> which represents the number of units that
fit in a pallet.
"""
class Custom_ProductTemplate_PedroLara(models.Model):
    _inherit = "product.template"

    udPallet = fields.Integer(
        'Unidades por palet', help='Número de unidades que caben en un palet', compute='_compute_udPallet',
        inverse='_set_udPallet', store=True)

    @api.depends('product_variant_ids', 'product_variant_ids.udPallet')
    def _compute_udPallet(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.udPallet = template.product_variant_ids.udPallet
        for template in (self - unique_variants):
            #ud_pallet = self.udPallet
            template.udPallet = 0

    @api.one
    def _set_udPallet(self):
        if len(self.product_variant_ids) == 1:
            self.product_variant_ids.udPallet = self.udPallet


    @api.model_create_multi
    def create(self, vals_list):
        # Override the original create function for the inherited model
        templates = super(Custom_ProductTemplate_PedroLara, self).create(vals_list)
        for template, vals in pycompat.izip(templates, vals_list):
            # Set udPallet value from form
            template.udPallet = vals.get('udPallet') or 0

        return templates

"""
This Class inherit ProductProduct from sales module to add a new
attribute << udPallet >>, same attribute added in ProductTemplate.
This attribute has been added here because each variant of a
product can have a different value of udPallet
"""
class Custom_ProductProduct_PedroLara(models.Model):
    _inherit = "product.product"
    udPallet = fields.Integer('Unidades por palet', help='Número de unidades que caben en un palet')


"""
This class inherit sale.order to add a field to count the sum of pallets of the order
"""
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pallet_total = fields.Float(string='Total palets', store=True, readonly=True, compute='_amount_all', track_visibility='always', track_sequence=6)

    @api.depends('order_line.price_total')
    def _amount_all(self):
        super(SaleOrder, self)._amount_all()
        for order in self:
            total_pallet = 0.0
            for line in order.order_line:
                total_pallet += line.pallet_qty
            order.update({
                'pallet_total': total_pallet
            })

    @api.multi
    def recalculate_prices(self):
        for line in self.mapped('order_line'):
            dict = line._convert_to_write(line.read()[0])
            if 'product_tmpl_id' in line._fields:
                dict['product_tmpl_id'] = line.product_tmpl_id
            line2 = self.env['sale.order.line'].new(dict)
            # we make this to isolate changed values:
            line2.product_uom_change()
            line2._onchange_discount()
            line.write({
                'price_unit': line2.price_unit,
                'discount': line2.discount,
                'udPallet': line2.udPallet
            })
        return True

    @api.multi
    def recalculate_names(self):
        for line in self.mapped('order_line').filtered('product_id'):
            # we make this to isolate changed values:
            line2 = self.env['sale.order.line'].new({
                'product_id': line.product_id,
            })
            line2.product_id_change()
            line.name = line2.name
        return True



"""
This class inherit sale.order.line to add two fields: one for number of units per
pallet and another one for the quantity of this product pallets in the order
"""
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Change description to add 'kg' to the variant products
    def get_sale_order_line_multiline_description_sale(self, product):
        res = super(SaleOrderLine,self).get_sale_order_line_multiline_description_sale(product)
        if res.endswith(')'):
            res = res[:-1] + ' kg)'
        return res

    udPallet = fields.Float('Unid Palet', readonly=True)#, compute='_compute_udPallet', inverse='_set_udPallet', default=0.0)
    pallet_qty = fields.Float('Palets', readonly=True, compute='_compute_amount')

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        super(SaleOrderLine,self)._compute_amount()
        for line in self:
            if line.udPallet > 0.:
                pallets = line.product_uom_qty / (1.*line.udPallet)
                line.update({'pallet_qty':pallets})

    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        super(SaleOrderLine,self).product_uom_change()
        if not self.product_uom or not self.product_id:
            return
        else:
            self.udPallet = self.product_id.udPallet


    @api.multi
    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine,self)._prepare_invoice_line(qty)
        res['udPallet'] = self.udPallet

        return res

    def _get_protected_fields(self):
        return super(SaleOrderLine,self)._get_protected_fields() + ['udPallet']

    @api.model_create_multi
    def create(self, vals_list):
        # Create lines by calling create from SaleOrderLine
        lines = super(SaleOrderLine, self).create(vals_list)
        
        # Update udPallet of line with udPallet of Product
        for line in lines:
            line.udPallet = line.product_id.udPallet
           
        return lines
