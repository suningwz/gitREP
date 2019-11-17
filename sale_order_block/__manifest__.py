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
    'name': "Sale Order Block",
    'version': '12.0.1.0.0',
    'summary': """Incoming email server validation""",
    'author': "Aswanth",
    'maintainer': 'Aswanth',
    'company': "Confianz",
    'website': "https://www.confianz.com",
    'category': 'Validation setting',
    'depends': ['base','sale_stock'],
    'data': [
                
                'views/sale_order_action.xml',
             
            ],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
