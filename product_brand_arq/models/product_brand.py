# # -*- coding: utf-8 -*-

# from odoo import fields, models

# class productBrand(models.Model):
#     _name = 'product.brand'

#     name = fields.Char(string='Marca',required=False)
# #nuevo
# class productModelo(models.Model):
#     _name = 'product.modelo'

#     name = fields.Char(string='Modelo',required=False)
# #termino

# class productTemplate(models.Model):
#     _inherit = 'product.template'

#     brand_id = fields.Many2one('product.brand',string='Marca')
#  #   modelo = fields.Char(string='Modelo')
#  	modelo = fields.Many2one('product.modelo',string='Modelo')

# -*- coding: utf-8 -*-

from odoo import fields, models

class productBrand(models.Model):
    _name = 'product.brand'

    name = fields.Char(string='Marca',required=False)

class productmodelo(models.Model):
    _name = 'product.modelo'

    name = fields.Char(string='Modelo',required=False)

class productTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand',string='Marca')
    modelo = fields.Many2one('product.modelo',string='Modelo')