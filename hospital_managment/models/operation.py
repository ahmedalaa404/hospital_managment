from odoo import models, fields, api


class Operation(models.Model):
    _name = 'operation.operation'
    _description = 'Operation'
    _log_access = False
    _rec_name = 'ref'

    doctor_id = fields.Many2one('res.users', string='Doctor')
    ref = fields.Char()
    operation_name = fields.Char()
    ref_record = fields.Reference(
        [('hospital.patient', 'patient'),
         ('hospital.appointments', 'appointments')],
        string='record')

    @api.model
    def name_create(self, name):
        return self.create({'operation_name': name}).name_get()[0]
