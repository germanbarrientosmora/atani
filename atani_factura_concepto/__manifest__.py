# -*- coding: utf-8 -*-
{
    'name': "atani_add_concepto_factura",

    'summary': """add_fields_in factura
    """,

    'description': """
        Modulo para para agregar campo de concepto en facturas
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale_management',
        'sale',
        'atani_ventas_addmarcamodelo',
        'account',

        ],

	'data': [
   'views/factura_addfield.xml',
   'views/report_factura_addfield.xml'
#    'data/categorias.xml',

    ],
	'demo':[

	],
    'installable':True,
}
