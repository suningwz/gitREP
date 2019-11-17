# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from datetime import date


class website_account(http.Controller):
    
    @http.route('/web/<partner_id>', type='http', auth='public', website=True) 
    def example_page(self,*args, **kw):
        partner_id = int(kw['partner_id'])
        print("\n\n",partner_id)
        Invoices = http.request.env['account.invoice']
        return request.render('invoice_email.WebInvoices', {
            'invoices': Invoices.search([('state','=','open'),('partner_id','=',partner_id),('type','=','out_invoice')])
        })
    
    @http.route('/web/invoice/approve',type='http', methods=['GET'], auth='public', website=True)
    def approve(self,**kw):
        for key in kw.values():
            source_rec = http.request.env['account.invoice'].search([('id','=',int(key))])
            rec_partner= source_rec.partner_id.id
            payment_rec=http.request.env['account.payment'].create({
                                                        'destination_journal_id': False, 
                                                        'partner_bank_account_id': False, 
                                                        'payment_date':str(date.today()), 
                                                        'journal_id': 7, 
                                                        'invoice_ids':[(6,0,source_rec.ids)],
                                                        'currency_id': 2, 
                                                        'partner_type': 'customer', 
                                                        'message_attachment_count': 0, 
                                                        'communication': source_rec.reference, 
                                                        'payment_method_id': 1, 
                                                        'partner_id': source_rec.partner_id.id, 
                                                        'amount': source_rec.amount_total_signed, 
                                                        'payment_type': 'inbound'    
                                                    })
            payment_rec.action_validate_invoice_payment()
        return http.request.redirect('/web/%d' %(rec_partner))
        