# -*- coding: utf-8 -*-
{
    'name': "pedro-lara-reports-comments",

    'summary': """
        Este módulo permite guardar dos campos de texto en la ficha de un cliente:
        """,

    'description': """
       Este módulo permite guardar dos campos de texto en la ficha de un cliente:
        - Nota para órdenes de venta
        - Nota para facturas (Uso especialmente para métodos de pago)
    """,
 
    'author': "Andrés García Castilla",
    'website': "https://www.linkedin.com/in/andgarcas/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_management', 'account', 'contacts'],

    # always loaded
    'data': [
        'views/views.xml',
    ]
    
}