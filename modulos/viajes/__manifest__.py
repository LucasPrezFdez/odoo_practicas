# -*- coding: utf-8 -*-
{
    'name': "viajes2",
    'summary': "Control y gestion de viajes realizados en vehiculos",
    'description': """
        Este modulo permite el control y la gestión de los viajes que realizan los pasajeros en vehiculos
    """,

    'author': "Lucas Perez",    
    'website': "github",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'viajes',
     'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/vehiculo.xml',
        'views/viaje.xml',
        'views/partner.xml',
        'views/parada.xml',
        'views/menus.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/demo.viajes.xml',
    ],
    'installable': True,
    'application': True
}