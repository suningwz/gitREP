# -*- coding: utf-8 -*-

from odoo import models , fields , api
import requests
import json
from datetime import date
class ResCompany(models.Model):
	_inherit ="res.company"

	tax_cloud_act = fields.Boolean()

class ResDiscountSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    so_tax_cloud = fields.Boolean(related = "company_id.tax_cloud_act",readonly=False )
    tax_cloud_id = fields.Char(config_parameter='tax_cloud_id')
    tax_cloud_key = fields.Char(config_parameter='tax_cloud_key')
    
    @api.multi
    def set_values(self):
        super(ResDiscountSettings, self).set_values()
        if not self.so_tax_cloud:
        	self.env['taxcloud.tic'].search([]).sudo().unlink()

    @api.multi
    def sync_taxcloud_category(self):
    	config_parm = self.env['ir.config_parameter']
    	input_data = {"apiLoginID": config_parm.get_param('tax_cloud_id'),"apiKey":config_parm.get_param('tax_cloud_key')}
    	resp = requests.post(url="https://api.taxcloud.com/1.0/TaxCloud/GetTICs", data = input_data)
    	tics_data = resp.json()
    	tic_category_data = [{'tic_code':i.get('TICID'),'name':i.get('Description')} for i in tics_data.get('TICs')]
    	tic_object = self.env['taxcloud.tic'].sudo()
    	for dictionary in tic_category_data:
    		tic_object.create(dictionary)
    	return True


class res_country(models.Model):
    _inherit = 'res.country.state'
 
    @api.multi
    def name_get(self):
        data = []
        for state in self:
            display_value = ''
            display_value += state.name or ""
            display_value += ' ['
            display_value += state.code or ""
            display_value += ']'
            data.append((state.id, display_value))
        return data

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        recs = self.browse()
        if not recs:
            recs = self.search([('code', operator, name)] + args, limit=limit)
        return recs.name_get()

class TaxcloudTic(models.Model):
	_name = 'taxcloud.tic'
	

	name = fields.Char(string = "Description")
	tic_code = fields.Char(string = "TIC code")
	
		
class ProductTemplate(models.Model):
	_inherit = "product.template"

	taxcloud_tic_ctg = fields.Many2one('taxcloud.tic', string="TaxCloud Category")

	

class SaleOrder(models.Model):
	_inherit = "sale.order"
    
	@api.multi
	def action_confirm(self):

		config_parm = self.env['ir.config_parameter']
		
		partner_id = self.partner_id
		

		addrs_data = {
		    "apiLoginID": config_parm.get_param('tax_cloud_id'),
		    "apiKey": config_parm.get_param('tax_cloud_key'),
		    "Address1": partner_id.street,
		    "Address2": partner_id.street2,
		    "City": partner_id.city,
		    "State": partner_id.state_id.code,
		    "Zip5": partner_id.zip,
		    "Zip4":""
		}

		resp = requests.post(url="https://api.taxcloud.com/1.0/TaxCloud/VerifyAddress", data=addrs_data)
		address_info = resp.json()
		company = self.env.user.company_id
		
		
		cart_items = [{"Qty":recrd.product_uom_qty,
					   "Price":recrd.price_unit,"TIC":recrd.product_id.taxcloud_tic_ctg.tic_code,
					   "ItemID":recrd.product_id.name,"Index":index} for index,recrd in enumerate(self.order_line)]
		loockup_data = {
					  "apiLoginID": config_parm.get_param('tax_cloud_id'),
		    		  "apiKey": config_parm.get_param('tax_cloud_key'),
					  "customerID": partner_id.name,
					  "deliveredBySeller": True,
					  "cartID": "",
					  "destination": {
								    "Address1": address_info.get('Address1'),
								    "City": address_info.get('City'),
								    "State": address_info.get('State'),
								    "Zip5": address_info.get('Zip5'),
								    "Zip4": address_info.get('Zip4')
					  					},
					  "origin": 	{
								    "Address1": address_info.get('Address1'),
								    "City": address_info.get('City'),
								    "State": address_info.get('State'),
								    "Zip5": address_info.get('Zip5'),
								    "Zip4": address_info.get('Zip4')
								  		},
					  "cartItems":cart_items
					}
		resp_lookup =requests.post("https://api.taxcloud.com/1.0/TaxCloud/Lookup",json=loockup_data)
		lookup_info = resp_lookup.json()
		tax_resp = lookup_info.get('CartItemsResponse')
		order_lines = self.order_line
		
		for line_tax in zip(order_lines,tax_resp):
			new_tax = (line_tax[1].get('TaxAmount')/line_tax[0].price_subtotal)*100
			tax_id = self.env['account.tax'].search([('name','ilike',str(new_tax)[0:4])])
			if  not tax_id: 
				tax_id = self.env['account.tax'].create({ 'name':"Tax %s"%(str(new_tax)[0:4]),
													  'amount':new_tax

													})
			line_tax[0].tax_id = tax_id
		super(SaleOrder,self).action_confirm()
		return True


