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
    sequence = fields.Integer(string='Sequence')

    @api.model
    def name_create(self, name):
        print(self)
        print(name)
        rec=self.create({'operation_name': name})

        print("rec",rec)
        namme=rec.name_get()[0]
        print(namme)
        return namme
