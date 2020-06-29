# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DollarConfigSettings(models.TransientModel):
    #_name = 'apps_odoo_com.settings'
    _inherit = 'res.config.settings'

    costo_dolares = fields.Boolean(string="Costo en Dolares")
    
    def set_values(self):
        res = super(DollarConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('moneda_utilidad_so.costo_dolares', self.costo_dolares)
        return res

    @api.model
    def get_values(self):
        res = super(DollarConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        costo_dolares_param = ICPSudo.get_param('moneda_utilidad_so.costo_dolares')
        res.update(costo_dolares=costo_dolares_param)
        return res
