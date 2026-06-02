from odoo import models,fields,api


class Operation(models.Model):
    _name = 'operation.operation'
    _description = 'Operation'
    _log_access=False
    _rec_name = 'ref'

    doctor_id=fields.Many2one('res.users',string='Doctor')
    ref=fields.Char()
