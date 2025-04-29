# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Ini adalah modul latihan Odoo 17 Sun Motor",

    'description': """
Deksirpsi modul hospital latihan Odoo 17 Sun Motor
    """,

    'author': "nurularifins",
    'website': "https://www.sunmotor.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Health',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
