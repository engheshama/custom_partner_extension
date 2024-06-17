from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    total_unpaid_invoices_amount = fields.Monetary(
        string="Total Unpaid Invoices Amount", 
        compute='_compute_total_unpaid_invoices_amount',
        currency_field='currency_id'
    )

    @api.depends('invoice_ids')
    def _compute_total_unpaid_invoices_amount(self):
        for partner in self:
            total = sum(invoice.amount_residual for invoice in partner.invoice_ids if invoice.move_type == 'out_invoice' and invoice.state == 'posted')
            partner.total_unpaid_invoices_amount = total
