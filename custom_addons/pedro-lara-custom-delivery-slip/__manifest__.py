# -*- coding: utf-8 -*-
{
    'name': "pedro-lara-custom-delivery-slip",

    'summary': """
        Este módulo personaliza los albaranes de entrega para PetMaxi
        """,

    'description': """
       
    """,
 
    'author': "Andrés García Castilla",
    'website': "https://www.linkedin.com/in/andgarcas/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock'],

    # always loaded
    'data': [
        'views/report.xml',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}