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
    'name': 'Invoice Email ',
    'summary': 'Listing the Paid Invoices',
    'author': 'Aswanth',
    'depends': ['base','account','website','sale'],
    'data': [   
                'views/assets.xml',
                'views/templates.xml',
                'views/invoice_mail_view.xml',
    	        'views/mail_template.xml',
                'views/sale_order_line_view.xml'
	],
    'installable': True,
    'application': True,
    'auto_install': False,
}
