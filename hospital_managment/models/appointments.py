from odoo import fields, models


class Appointments(models.Model):
    _name = 'hospital.appointments'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Appointments'

    name = fields.Char(string="Name", tracking=1)
    patient_id = fields.Many2one('hospital.patient')
    gender = fields.Selection(related='patient_id.gender', string="Gender", readonly=False)
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now, tracking=1)
    booking_date = fields.Date(string="Booking Date", tracking=1, default=fields.Date.context_today)
    doctor_id = fields.Many2one('res.users', string="Doctor", tracking=1)
    status = fields.Selection(
        [('draft', 'Draft'),
         ('in_process', 'In-Process'),
         ('done', 'Done'),
         ('cancel', 'Cancel'),
         ], default='draft',
    )

    priority=fields.Selection(
        [
            ('0','low'),
            ('1','medium'),
            ('2','height')
        ]
    )

    def action_test(self):
        return {
            'effect': {
                'message': "test action for rainbow man ",
                'type': 'rainbow_man',
                'fadeout': 'slow'
            }
        }

    def set_draft(self):
        for rec in self:
            rec.status = 'draft'

    def set_in_process(self):
        for rec in self:
            rec.status = 'in_process'

    def set_cancel(self):
        for rec in self:
            rec.status = 'cancel'

    def set_done(self):
        for rec in self:
            rec.status = 'done'

class AppointmentsPharmacy(models.Model):
    _name = 'hospital.appointments.pharmacy'
    _description = 'Appointments Pharmacy'

    name=fields.Char(string="Name", tracking=1)