# -*- coding: utf-8 -*-

from odoo import fields, models

class product_camposrelated(models.Model):
    _inherit = 'product.product'


    x_brand= fields.Many2one(related='product_tmpl_id.brand_id')#campo que esta relacionado + el campo que queremos del otro modelo

   # x_modelo= fields.Char(related='product_tmpl_id.modelo')
    x_modelo= fields.Many2one(related='product_tmpl_id.modelo')