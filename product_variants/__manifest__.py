# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
##############################################################################      
#         _______  _____            _______  _       _______
#         |     | |       |       | |     | | \    |    |    |     |
#         |_____| |_____  |   _   | |_____| |  \   |    |    |_____|
#         |     |       | |  / \  | |     | |   \  |    |    |     |
#         |     |  _____| |_/   \_| |     | |    \_|    |    |     |
#                 
##############################################################################


{
    'name': 'product varient',
    'version': '12.0.1.0.0',
    'summary': 'product varient',
    'author': 'Confianz Global,Inc.',
    'description': """
                """,
    'depends': ['base','sale','product'],
    'category': 'Hidden',
    'sequence': 20,
    'data': [
        'views/sale_view.xml',
        'security/ir.model.access.csv'
    ],
    'test': [
    ],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
