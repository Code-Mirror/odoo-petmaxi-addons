# -*- coding: utf-8 -*-
{
    'name': "pedro-lara-custom-invoice-analysis",

    'summary': """
        Este módulo permite generar un reporte de análisis de facturas como lo requiere Pedro Lara.
        """,

    'description': """
       Este módulo añade:
        - Campo para guardar el código de autorización SEPA para cada cliente.
        - Añade el capo a la vista list de Facturas
    """,
 
    'author': "Andrés García (@garcicasti) & Pedro Lara-Benitez (@pedrolarben)",
    'website': "https://www.linkedin.com/in/andgarcas/ http://www.pedrolarben.com",

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