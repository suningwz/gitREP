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
    'name': 'Tax Cloud  Api integration 1.0',
    'summary': 'Tax cloud api integration',
    'version': '12.0.1.1.0',
    'author': 'AswanthBabu',
    'category': 'Tools',
    'depends': ['base','account','sale'],
    'data': [  
                'security/ir.model.access.csv',
    	        'views/res_config_view.xml',        
	],
    'images': ['static/description/icon.png'],
    'installable': True,
    'license': 'AGPL-3',
    'application': True,
    'auto_install': False,
}
