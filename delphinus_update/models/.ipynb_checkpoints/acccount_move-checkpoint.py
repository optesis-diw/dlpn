from odoo import api, fields, models, _
from num2words import num2words


class AccountMove(models.Model):
    _inherit= "account.move"
    
     
    invoice_line_ids = fields.One2many('account.move.line', 'move_id', string='Invoice lines',
        copy=False, readonly=True,
        domain=[('exclude_from_invoice_tab', '=', False)],
        states={'draft': [('readonly', False)]})
    
    quantity = fields.Float(string='Poids',default=1.0, related="invoice_line_ids.quantity")
    
    quantity_poids_total = fields.Float(string='somme des poids', compute="_quantity_poids_total")
    
    
    
    @api.onchange('quantity', 'invoice_line_ids')
    def _quantity_poids_total(self):
        for rec in self:
            total = sum(rec.invoice_line_ids.mapped('quantity'))
            rec.quantity_poids_total = total
        

  