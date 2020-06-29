# -*- coding: utf-8 -*-

from odoo import api, fields, models
#from odoo.addons import decimal_precision as dp


class SaleOrderLine(models.Model):
    
    _inherit = "sale.order.line"

    en_dolares = fields.Boolean(string='Costo en Dolares',
                                    compute="es_costo_dolar",
                                    )

    def _compute_margin(self, order_id, product_id, product_uom_id):
        frm_cur = self.env.user.company_id.currency_id
        to_cur = order_id.pricelist_id.currency_id
        if self.en_dolares:
            print('Esta en dolares')
            to_cur = frm_cur
        purchase_price = product_id.standard_price
        if product_uom_id != product_id.uom_id:
            purchase_price = product_id.uom_id._compute_price(purchase_price, product_uom_id)
        price = frm_cur._convert(
            purchase_price, to_cur, order_id.company_id, order_id.date_order or fields.Date.today(), round=False)
        return price

    @api.model
    def es_costo_dolar(self):
        ICPSudo = self.env['ir.config_parameter'].sudo()
        costo_dolares_param = ICPSudo.get_param('moneda_utilidad_so.costo_dolares')
        self.en_dolares = costo_dolares_param
     