# -*- coding: utf-8 -*-

from odoo import models , fields , api

class InvoiceEmail(models.Model) :
    
    _inherit = 'account.invoice' 
    
    state = fields.Selection(selection_add=[('approved', 'Approved')])
    
#Send Open Invoices Mail 

    @api.multi
    def send_invoice(self):
    
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            email_template_id = ir_model_data.get_object_reference('invoice_email', 'invoice_mail_template_id')[1]
        except ValueError:
            email_template_id   = False
        try:
            form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            form_id = False
        context = {
            'default_model': 'account.invoice',
            'default_res_id': self.ids[0],
            'default_use_template': bool(email_template_id),
            'default_template_id': email_template_id ,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'force_email': True
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(form_id, 'form')],
            'view_id': form_id,
            'target': 'new',
            'context': context,
        }


