# -*- coding: utf-8 -*-
#╔══════════════════════════════════════════════════════════════════╗
#║                                                                  ║
#║                ╔═══╦╗       ╔╗  ╔╗     ╔═══╦═══╗                 ║
#║                ║╔═╗║║       ║║ ╔╝╚╗    ║╔═╗║╔═╗║                 ║
#║                ║║ ║║║╔╗╔╦╦══╣╚═╬╗╔╬╗ ╔╗║║ ╚╣╚══╗                 ║
#║                ║╚═╝║║║╚╝╠╣╔╗║╔╗║║║║║ ║║║║ ╔╬══╗║                 ║
#║                ║╔═╗║╚╣║║║║╚╝║║║║║╚╣╚═╝║║╚═╝║╚═╝║                 ║
#║                ╚╝ ╚╩═╩╩╩╩╩═╗╠╝╚╝╚═╩═╗╔╝╚═══╩═══╝                 ║
#║                          ╔═╝║     ╔═╝║                           ║
#║                          ╚══╝     ╚══╝                           ║
#║ SOFTWARE DEVELOPED AND SUPPORTED BY ALMIGHTY CONSULTING SERVICES ║
#║                   COPYRIGHT (C) 2016 - TODAY                     ║
#║                   http://www.almightycs.com                      ║
#║                                                                  ║
#╚══════════════════════════════════════════════════════════════════╝
{
    'name': 'Merge Multiple Invoices',
    'summary': """Allow your users to Merge Multiple Invoices.""",
    'description': """
        Allow your users to Merge Mutiple Invoices of the same customer.
        merge invoice invoices mergeing invoice mergeing merge invoices merging invoice merging invoices

        Autorisez vos utilisateurs à fusionner plusieurs factures du même client. 
        Fusionner les factures Fusionner les factures Fusionner les factures Fusionner les factures Fusionner les factures Fusionner les factures

        Erlauben Sie Ihren Benutzern, mehrere Rechnungen desselben Kunden zusammenzuführen.
        Rechnungen zusammenführen Rechnungen zusammenführen Zusammenführen Rechnungen zusammenführen Rechnungen zusammenführen

        Permita que sus usuarios fusionen las facturas múltiples del mismo cliente. 
        fusionar facturas facturas fusionar factura fusionar fusionar facturas fusionar factura fusionar facturas

        Sta uw gebruikers toe om Mutiple-facturen van dezelfde klant samen te voegen. 
        samenvoegen factuur facturen samenvoegen factuur samenvoegen samenvoegen facturen samenvoegen factuur samenvoegen facturen
    """,
    'version': '1.0.1',
    'category': 'Accounting',
    'author': 'Almighty Consulting Services',
    'website': 'https://www.almightycs.com',
    'license': 'OPL-1',
    'depends': ["account"],
    'data' : [
        'wizard/merge_wizard_view.xml',
    ],
    'images': [
        'static/description/acs_merge_invoice_almightycs_cover.jpg',
    ],
    'installable': True,
    'sequence': 1,
    'price': 12,
    'currency': 'EUR',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: