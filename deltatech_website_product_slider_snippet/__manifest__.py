# -*- coding: utf-8 -*-
# ©  2015-2020 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details
{
    'name': 'eCommerce Product Slider',
    'category': 'Website',
    'summary': 'eCommerce extension',

    'version': '13.0.1.0.0',

    "author": "Terrabit, Dorin Hongu",
    "website": "https://www.terrabit.ro",

    'depends': ['website_sale','deltatech_product_list'],
    'data': [
        'views/templates.xml',
        'views/snippets.xml',
    ],

    "images": ['/static/description/main_screenshot.png'],
    "installable": True,
    'qweb': ['static/src/xml/*.xml'],
}
