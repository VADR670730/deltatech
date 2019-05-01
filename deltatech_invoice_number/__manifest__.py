# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    "name": "Invoice Number",
    'version': '11.0.1.0.0',
    "author": "Terrabit, Dorin Hongu",
    "website": "www.terrabit.ro",
    "description": """

Functions:
----------

 - At the validation, the invoice date must be greater than the last invoice validated
 - The number of the invoice can be modified
 - A number can be allocated to a invoice in the draft state. After the number is allocated, the date of the invoice cannot be changed
 - The user must be in the account.group_account_invoice group (Accounting & Finance / Billing)

Functionalitati:
----------------

 - Validare data factura sa fie mai mare decat data din ultima factura
 - Posibilitatea de a modifica numarul unei facturi pentru un anumit grup de utilizatori
 - posibilitatea de a numerota o factura chiar daca aceasta nu este validata. Dupa numerotare nu se mai poate modifca data


    """,
    "category": "Accounting",
    "depends": ["account_invoicing"],

    "license": "LGPL-3",

    "data": [
        'security/sale_security.xml',
        'views/account_invoice_view.xml',
        'wizard/account_invoice_change_number_view.xml'
    ],

    "installable": True,
}
