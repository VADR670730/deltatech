# -*- coding: utf-8 -*-
# ©  2008-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details



{
    'name': "Product List",
    'version': '13.0.1.0.0',
    'category': 'Sale',
    "author": "Terrabit, Dorin Hongu",
    'company': 'Terrabit',
    'maintainer': 'Terrabit',
    'website': "https://www.terrabit.ro",
    'depends': ['product','sale'],
    'data': [
        'views/product_list_view.xml',
        'security/ir.model.access.csv'
    ],
    "images": ['static/description/main_screenshot.png'],
    'license': "AGPL-3",
    'installable': True,
    'application': False,
}
