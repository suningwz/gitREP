# -*- coding: utf-8 -*-
{
    'name': "automated_product_creation 1.0",

    'summary': """
        This module help to  create product using CRON""",

    'description': """
        CRON Product Creation
    """,

    'author': "AswanthBabu",
    'category': 'Tools',
    'version': '12.0.1.1.0',

    'depends': ['base','product'],

    
    'data': [
       
        'data/scheduler_action.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'license': 'AGPL-3',
    'application': True,
    'auto_install': False,
   
}