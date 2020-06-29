# -*- coding: utf-8 -*-
{
    'name': "moneda_utilidad_so",

    'summary': """
        Omite la conversión a Pesos cuando la tarifa es Dolares
        """,

    'description': """
        Omite la conversión de campo Coste (en las líneas) a Pesos cuando la tarifa es Dolares en las SO 
    """,

    'author': "Soluciones 4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_margin'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/config_settings.xml',
        #'views/templates.xml',
    ],
}