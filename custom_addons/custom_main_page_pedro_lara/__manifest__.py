# -*- coding: utf-8 -*-
{
    'name': "customMainPagePedroLara",

    'summary': """
        Añade página principal para ser usada por el comercial.""",

    'description': """

    """,

    'author': "Andrés García Castilla",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    
}
