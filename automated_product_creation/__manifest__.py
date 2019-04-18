
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
    
    'name': 'Automated Product Creation',
    'summary': 'This module help to  create product using CRON',
    'author': 'Aswanth',
    'version': '12.0.1.1.0',
    'category': 'Tools',
    'depends': ['base','product'],
     'data': [
       
        'data/scheduler_action.xml',
    ],
   	'images': ['static/description/icon.png'],
   	'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}

