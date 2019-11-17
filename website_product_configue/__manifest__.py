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
    'name': "website_product_configue",
    'description': """
        Long description of module's purpose
    """,
    'author': "Aswanth",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '12.0.1.0.0',
    'depends': ['base','website_sale','product'],
    'data': [
        'views/product_views.xml',
        'views/product_templates.xml',
    ],  
}