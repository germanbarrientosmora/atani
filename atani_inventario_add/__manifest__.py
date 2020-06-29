# -*- coding: utf-8 -*-
{
    'name': "Marca y modelo vista lista",
    'description': """
        Mostrar el tipo de marca y modelo en el modulo de inventario en la vista lista
        Mostar el tipo de marca y modelo en ajuste de inventario para que sus busquedan puedan hacerlas desde modelo y marca
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    'depends': [
                'base',
                'stock',
                'purchase',
                'product_brand_arq',
                ],
    'data': [
       
        'views/productos_lista.xml',
        'views/stock_invetary.xml',
        


        

        ],
    'installable':True,
    'auto_install':False,
}
