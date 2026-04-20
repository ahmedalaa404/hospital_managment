from odoo import fields ,models


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    name=fields.Char(string="Name")
    user_confirm_id=fields.Many2one('res.users')