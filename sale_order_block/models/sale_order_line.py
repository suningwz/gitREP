# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api,_


class SaleOrderLine(models.Model):
    """Sale Order Block"""
    _inherit = 'sale.order.line'
    
    order_key = fields.Selection([('yes', 'Yes'), ('no', 'No')], 'Order Key', required=True, default = 'yes')
    product_barcode = fields.Char(related="product_id.barcode", store=True, readonly= False)
    b_code = fields.Char(compute='get_length',string='Length',store=True)

   
    @api.multi
    def _action_launch_stock_rule(self):
        return super(SaleOrderLine,self.filtered(lambda r:r.order_key == 'yes'))._action_launch_stock_rule()
    @api.multi
    @api.onchange('product_barcode')
    def product_barcode_onchange(self):
        if self.product_barcode:
            prd = self.env['product.product'].search([('barcode','=',self.product_barcode)])
            print("\n\n\n",prd)
            self.product_id = prd.id
    @api.one       
    @api.depends('product_barcode')
    def get_length(self):
        
        if self.product_barcode:
            self.b_code=self.product_barcode
            
    @api.one          
    def print_self_one(self):
        print(self)

    @api.multi
    def print_self_multi(self):
        self.ensure_one()
        print(self)