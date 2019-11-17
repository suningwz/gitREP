# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError
from datetime import date


class payment_wizard(models.TransientModel):
	_name = 'saleorder.account.register.payment'	
	
	invoice_ids = fields.Many2many('account.invoice', string = "Invoices")
	@api.model
	def default_get(self,fields):
		active_keys = self._context.get('active_ids')
		if active_keys:
			if len(set(self.env['sale.order'].browse(active_keys).mapped("partner_invoice_id").ids)) !=1:
				raise UserError("Cannot Initiate payment for different Invoice Address")
			invoice_ids = self.env['sale.order'].browse(active_keys).mapped("invoice_ids").ids
			rec = dict()
			rec[fields[0]] = [(6,0,invoice_ids)]
			return rec
	@api.multi  
	def create_payments(self):
		journal = self.env['account.journal'].search([('name','=','Bank')])
		for invoice in self.invoice_ids:
			payment_rec = self.env['account.payment'].create({
                                                        'payment_date':str(date.today()), 
                                                        'journal_id': journal.id, 
                                                        'invoice_ids':[(6,0,invoice.ids)],
                                                        'currency_id': 2, 
                                                        'partner_type': 'customer', 
                                                        'message_attachment_count': 0, 
                                                        'communication': invoice.reference, 
                                                        'payment_method_id': 1, 
                                                        'partner_id': invoice.partner_id.id, 
                                                        'amount': invoice.amount_total_signed, 
                                                        'payment_type': 'inbound'    
                                                    })
			payment_rec.post()