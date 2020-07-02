# -*- coding: utf-8 -*-
{
    'name': "customSalesPedroLara",

    'summary': """
        Este modulo permite vender siguiendo las tarifas de Pedro Lara en Odoo.""",

    'description': """
        Las listas de precios en Odoo no tienen en cuenta el total de productos en 1 sola orden de ventas.
        Por ejemplo, podríamos tener una tienda de camisetas y hacer un descuento por cantidad, pero no sólo de 1 modelo de camiseta,
        sino de cualquier combinación de camisetas. De este caso de uso se encarga este módulo.
        Además se añade paletización.
    """,

    'author': "Andrés García Castilla",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','product', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
