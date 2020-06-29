 #- * - coding: utf-8 - * -

from odoo import api
from odoo import fields
from odoo import models

class purchase_stock_recepcion(models.Model):
    _inherit = 'stock.inventory.line'

    @api.onchange('product_id')
    def _compute_costo_quilate_usd(self):
        
        id_x= self.env['product.template'].search([('id', '=', self.product_id.product_tmpl_id.id)],limit=1)
        #print(id_x)
        #modelo=self.env['product.product'].search(['product_tmpl_id','=',id_x])
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
            self.x_xmodelo=busqueda.modelo
        
            self.product_id=busqueda.product_variant_id

   

   # @api.model
    @api.model_create_multi
    def create(self, vals_list): #modificamos el create para agregar modelo y marca segun el producto agregado en inventario
       
        busqueda = self.env['product.template'].search([('id', '=',self.product_id.id)], limit=1)
        print(busqueda.brand_id.name)
        print(busqueda.brand_id.id)
        print(vals_list)                 
        #[{'inventory_id': 16, 'product_id': 2161, 'location_id': 12, 'product_uom_id': 1}]
        for values in vals_list:
            busquedas = self.env['product.template'].search([('id', '=',values['product_id'])], limit=1)
            print(busquedas.brand_id.name)
            print(busquedas.brand_id.id)
            values['x_xmarca']=busquedas.brand_id.id
            values['x_xmodelo']=busquedas.modelo.id  #se agregan los productos correspondientes a cada uno
        print(vals_list)
        res = super(purchase_stock_recepcion, self).create(vals_list)
      
        return res

   # x_xmodelo = fields.Char(string='Modelo')
    x_xmodelo = fields.Many2one('product.modelo',string='Modelo')
    x_xmarca = fields.Many2one('product.brand',string='Marca')

    product_id = fields.Many2one(
        'product.product', 'Product',
        domain=[('type', '=', 'product')],
        index=True, required=True)
