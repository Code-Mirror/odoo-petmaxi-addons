# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class StockPicking(models.Model):
	_inherit = 'stock.picking'

	stock_total_weight = fields.Float(string="Total Weight",compute='_total_weight_')
	
	@api.multi
	def _total_weight_(self):
		for res in self:
			total = 0
			for move_line in res.move_lines:
				total += move_line.stock_weight
			res.stock_total_weight = total

class StockMoveLine(models.Model):
	_inherit = 'stock.move'

	stock_weight = fields.Float(string="Weight",compute='_weight')

	@api.multi
	def _weight(self):
		for res in self:
			product_weight = res.product_id.weight
			quantity = res.quantity_done
			if not res.product_uom.factor == 0:
				if not res.product_uom.uom_type == "reference":
					quantity = quantity / res.product_uom.factor
			if quantity == 0:
				quantity = res.product_uom_qty
			res.stock_weight =product_weight * quantity