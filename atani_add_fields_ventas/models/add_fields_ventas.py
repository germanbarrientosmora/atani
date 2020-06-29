# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class add_fields(models.Model):
	"""docstring for ClassName"""
	_inherit='sale.order'


	x_concepto=fields.Char(
						String="x_concepto",
						)
	
	seleccion = fields.Boolean()# campo para seleccionar