# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class ProductProduct(models.Model):
    _inherit = "product.product"
    _order = 'date_deliver'
    
    website_order = fields.Boolean('website order', default=False)   
    date_deliver = fields.Date(string="End Date")
 
