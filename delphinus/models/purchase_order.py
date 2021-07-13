from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
       
                
    collecteur_id = fields.Many2one('optesis.collecteur.line', string='Collecteur')
    lieu_id = fields.Many2one('optesis.lieu.line', string='Lieu de Peche')

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"
    
    

    section_frais = fields.Selection([('filet', 'Filet'), ('entier', 'Entier')], string="Section Frais")
    calibre = fields.Many2one('optesis.calibre', string='Calibre')
    
    @api.model
    def _prepare_account_move_line(self, move):
        self.ensure_one()
        if self.product_id.purchase_method == 'purchase':
            qty = self.product_qty - self.qty_invoiced
        else:
            qty = self.qty_received - self.qty_invoiced
        if float_compare(qty, 0.0, precision_rounding=self.product_uom.rounding) <= 0:
            qty = 0.0

        _logger.info('Anta a %s with vals %s', self.calibre)
        return {
            'name': '%s: %s' % (self.order_id.name, self.name),
            'move_id': move.id,
            'currency_id': move.currency_id.id,
            'purchase_line_id': self.id,
            'date_maturity': move.invoice_date_due,
            'product_uom_id': self.product_uom.id,
            'product_id': self.product_id.id,
            'price_unit': self.price_unit,
            'calibre':self.calibre,
            'quantity': qty,
            'partner_id': move.commercial_partner_id.id,
            'analytic_account_id': self.account_analytic_id.id,
            'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
            'tax_ids': [(6, 0, self.taxes_id.ids)],
            'display_type': self.display_type,
        }
    

