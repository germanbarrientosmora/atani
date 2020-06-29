# -*- coding: utf-8 -*-
{
    'name': "Marca y modelo en inventario",
    'description': """
        Mostrar el tipo de marca y modelo en el modulo de inventario en la seccion de recepciones
        Mostar el tipo de marca y modelo en el modulo de compras
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
       
        'views/compra_add_modelo_marca.xml',
        'views/reporte_compras.xml',
        'views/reporte_pedido_compra.xml',
        'views/reporte_inventario.xml',
        'views/inventario_recepciones.xml',
        'views/reporte_vale_entrega.xml',

        ],
    'installable':True,
    'auto_install':False,
}
