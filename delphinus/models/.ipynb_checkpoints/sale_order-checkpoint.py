from odoo import api, fields, models, _
class saleOrder(models.Model):
    _inherit = "sale.order"
    
 
    
    order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True)
    
        
    product_uom_qty = fields.Float(string='Poids', digits='Product Unit of Measure', required=True, related="order_line.product_uom_qty")
    
    product_uom_qty_total = fields.Float(string='Somme des poids', digits='Product Unit of Measure', compute="_poids_total")
    
    
    
    @api.onchange('product_uom_qty', 'order_line')
    def _poids_total(self):
        for rec in self:
            total = sum(rec.order_line.mapped('product_uom_qty'))
            rec.product_uom_qty_total = total
            
            
    name_currency = fields.Char(related="currency_id.name")
    
    amount_total_cfa_euro = fields.Float(string='Total cfa', compute="_amount_total_cfa_euro_vente", widget="monetary")
   
    
    @api.onchange('amount_total', 'currency_id')
    def _amount_total_cfa_euro_vente(self):
        for rec in self:
            if rec.name_currency == 'EUR':
                rec.amount_total_cfa_euro = rec.amount_total * 605
            else:
                rec.amount_total_cfa_euro = rec.amount_total            
            
class saleOrderrLine(models.Model):
    _inherit = "sale.order.line"            