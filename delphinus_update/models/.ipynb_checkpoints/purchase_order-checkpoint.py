from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
   
    order_line = fields.One2many('purchase.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True)
    
        
    product_qty = fields.Float(string='Poids', digits='Product Unit of Measure', required=True, related="order_line.product_qty")
    
    product_qty_total = fields.Float(string='Somme de poids', digits='Product Unit of Measure', compute="_poids_achat_total")
    
   
    
    
    @api.onchange('product_qty', 'order_line')
    def _poids_achat_total(self):
        for rec in self:
            total = sum(rec.order_line.mapped('product_qty'))
            rec.product_qty_total = total

    
    name_currency = fields.Char(related="currency_id.name")
    
    amount_total_cfa = fields.Float(string='Total cfa', compute="_amount_total_cfa")
   
    
    @api.onchange('amount_total', 'currency_id')
    def _amount_total_cfa(self):
        for rec in self:
            if rec.name_currency == 'XOF':
                rec.amount_total_cfa = rec.amount_total
            else:
                rec.amount_total_cfa = 0  
            
                
    amount_total_euro = fields.Float(string='Total euro', compute="_amount_total_euro")
   
    
    @api.onchange('amount_total', 'currency_id')
    def _amount_total_euro(self):
        for rec in self:
            if rec.name_currency == 'EUR':
                rec.amount_total_euro = rec.amount_total
            else:
                rec.amount_total_euro = 0
                
    amount_total_cfa_euro = fields.Float(string='Total cfa', compute="_amount_total_cfa_euro", widget="monetary")
   
    
    @api.onchange('amount_total', 'currency_id')
    def _amount_total_cfa_euro(self):
        for rec in self:
            if rec.name_currency == 'EUR':
                rec.amount_total_cfa_euro = rec.amount_total * 655.93
            else:
                rec.amount_total_cfa_euro = rec.amount_total              
                
   
   

class PurchaseOrderLine_new(models.Model):
    _inherit = "purchase.order.line"
    
    
    lieu_collecte_ids = fields.Many2one('lb.lieu_collecte', string="Lieu de collecte")
    

   
    
class Type(models.Model):
    _name = 'lb.lieu_collecte'
    _rec_name = 'name'

    name = fields.Char(string="Lieu collecte")
    
    