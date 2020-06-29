# - * - coding: utf-8 - * -

from odoo import api
from odoo import fields
from odoo import models

class purchase_addfields_modelPurchase(models.Model):
    _inherit = 'purchase.order.line'


    @api.onchange('product_id')
    def _compute_product(self):
        
        id_x= self.env['product.template'].search([('id', '=', self.product_id.product_tmpl_id.id)],limit=1)
        #print(id_x)
        #modelo=self.env['product.product'].search(['product_tmpl_id','=',id_x])
        print("metodo de product id")
        print("self")
        print(self.x_xmarca)
        print(self.x_xmodelo)
        self.x_xmodelo=id_x.modelo
        self.x_xmarca=id_x.brand_id
        #como se obtuve eb id_x el id de product.template entonces ya podemos accesar con ese id a su modelo y marca de product product porque 
        #estan los cmapos relacionales en product product para product template.


    @api.onchange('x_xmodelo')
    def _onchange_modelo(self):
        busqueda = self.env['product.template'].search([('modelo', '=', self.x_xmodelo.name)], limit=1)
        print("modelo")
        print(busqueda.modelo.name)
        print("marca")
        print(busqueda.brand_id.name)
        if(busqueda.modelo.name != False):
            self.x_xmarca=busqueda.brand_id
            self.product_id=busqueda.product_variant_id
        #self.x_xmarca=busqueda.brand_id.name
        #self.x_xmodelo=busqueda.brand_id.name


        #self.product_id=busqueda.name


   
    x_xmarca= fields.Many2one(related='product_id.brand_id')#campo que esta relacionado + el campo que queremos del otro modelo

   # x_modelo= fields.Char(related='product_tmpl_id.modelo')
    x_xmodelo= fields.Many2one(related='product_id.modelo')