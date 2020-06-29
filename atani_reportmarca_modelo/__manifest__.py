# -*- coding: utf-8 -*-
{
    'name': "atani_add_modelo_marca_report_ventas",

    'summary': """add_fields_in report
    """,

    'description': """
        Modulo para ventas agregar en reporte los campos de modelo y marca.
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
        'atani_ventas_addmarcamodelo'

        ],

	'data': [
   'views/report_sale_modelomarca.xml',
#    'data/categorias.xml',

    ],
	'demo':[

	],
    'installable':True,
}
