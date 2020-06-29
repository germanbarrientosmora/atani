# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models, api

class CmotoaddField(models.Model):
    _inherit = 'account.invoice'

   
    x_id_order_invoice = fields.Many2one('sale.order',string='id_factura')#se crea un campo many to one relaciona con sale order
        #esto para poder hacer el campo relacionado


 #   x_concepto_x=fields.Char(related='x_id_order_invoice.x_concepto')   #nose puede ocupar este campo relacionado porque se pierde que factura pertenee a sale order                             
    #x_concepto_x=fields.Char()
    
    x_conceptox=fields.Char(compute='_compute_name',string='Concepto')
   
    #se pone la funcion computada y se busca en la sale order el nombre de esta que es la que lo identifica y se compara si es la misma que origin que es con la que se identifica la factura y si so iguales
    
    @api.multi
    def _compute_name(self):
        id_x= self.env['sale.order'].search([('name', '=', self.origin)])
        self.x_conceptox=id_x.x_concepto
      