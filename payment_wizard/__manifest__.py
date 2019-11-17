# -*- coding: utf-8 -*-
##############################################################################      
#         _______  _____            _______  _       _______
#         |     | |       |       | |     | | \    |    |    |     |
#         |_____| |_____  |   _   | |_____| |  \   |    |    |_____|
#         |     |       | |  / \  | |     | |   \  |    |    |     |
#         |     |  _____| |_/   \_| |     | |    \_|    |    |     |
#                 
##############################################################################

{
    'name': "payment_wizard",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Aswanth",
    'website': "http://www.yourcompany.com",

    'category': 'PaymentWizard',
    'version': '0.1',

   
    'depends': ['base','sale','account'],

   
    'data': [
        
        'views/sale_order_payment_wizard.xml',
    ],
   
}