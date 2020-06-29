# -*- coding: utf-8 -*-
{
    'name': "Marca y modelo en ventas",
    'description': """
        Mostrar el tipo de marcar y modelo para los productos
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    'depends': [
                'base',
                'sale_management',
                'sale',
                'stock',
                'product_brand_arq',
                'product'
                ],
    'data': [
        'views/sale_marca_modelo.xml',

        ],
    'installable':True,
    'auto_install':False,
}
