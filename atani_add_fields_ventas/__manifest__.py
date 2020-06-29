# -*- coding: utf-8 -*-
{
    'name': "atani_add_fields ventas productos",

    'summary': """add_fields
    """,

    'description': """
        Modulo para ventas agregar 1 campo en ventas, campoconcepto de venta.
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

        ],

	'data': [
   'views/atani_addd_fields_ventas.xml',
   'views/reporte_sale_order.xml'
#    'data/categorias.xml',

    ],
	'demo':[

	],
    'installable':True,
}
