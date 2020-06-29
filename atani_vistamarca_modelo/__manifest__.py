# -*- coding: utf-8 -*-
{
    'name': "Marca en inventario",
    'description': """
        Agregar marcas o eliminar marcas
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    'depends': [
                'base',
                'stock',
                'product_brand_arq',
                'product'
                ],
    'data': [
        'views/atani_add_marca.xml',
        'views/atani_add_modelo.xml',

        ],
    'installable':True,
    'auto_install':False,
}
