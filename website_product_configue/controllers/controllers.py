# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WebsiteProductConfigue(http.Controller):
	
	@http.route('/web/product/conf', methods=['GET'], auth='public', website=True)
	def list(self, **kw):
		print("\n\n\n\n",kw)
		pd_id = int(kw.get('product_id'))
		product = http.request.env['product.template'].browse(pd_id)
		
		atr_ids = product.attribute_line_ids
		values = []
		for attr_id in atr_ids:
			val = kw.get(str(attr_id.id))
			line_val =  http.request.env['product.attribute.value'].search([('name','ilike',val)])
			if not line_val:
				line_val =  http.request.env['product.attribute.value'].create({'attribute_id':attr_id.attribute_id.id,'name':val})
				dict_rec = {'attribute_line_ids': [[1, attr_id.id, {'value_ids': [(4,line_val.id)]}]]}
				product.write(dict_rec)  
			values.append(line_val.id)
			          
		prod_ids= product.mapped('product_variant_ids')
		for vals in prod_ids:
			if set(vals.attribute_value_ids.ids) == set(values):
				vals.write({'date_deliver':kw.get('date'),'website_order':True})
				return http.request.redirect('/shop/product/%s-%d' %(product.name.replace(" ","-"),product.id))