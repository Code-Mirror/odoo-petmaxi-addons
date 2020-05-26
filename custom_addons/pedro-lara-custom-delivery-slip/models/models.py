# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class pedrolara_customStockPicking(models.Model):
    _inherit = 'stock.picking'

    pallet_total = fields.Float(
        'Total pallets',
        readonly=True,
        compute='_compute_total_pallets_amount'
    )

    # When the sent units change, we recalculate pallet amounts.
    @api.onchange('product_uom_qty')
    def _compute_total_pallets_amount(self):

        for picking in self:
            total_pallet = 0.0
            for line in picking.move_lines:
                total_pallet += line.pallet_quantity
            picking.update({
                'pallet_total': total_pallet
            })


class pedrolara_customMoveLines(models.Model):
    _inherit = 'stock.move'
    pallet_quantity = fields.Float('Palets', readonly=True, compute='_compute_pallets_amount')
    units_per_pallet = fields.Integer(related='product_id.udPallet', string='Ud por pallet', readonly=True)
    product_barcode = fields.Char(related='product_id.barcode', string='Código de barras', readonly=True)
    product_unit_weight = fields.Float(related='product_id.weight', string='Kg/Unid', readonly=True)
   
    
    @api.onchange('product_uom_qty')
    def _compute_pallets_amount(self):
        
        for line in self:
            if line.units_per_pallet > 0.:
                pallets = line.product_qty / (1.*line.units_per_pallet)
                line.update({'pallet_quantity':pallets})
    

    