from odoo import fields, models, api


class Appointments(models.Model):
    _name = 'hospital.appointments'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Appointments'
    _rec_name='gender'




    name = fields.Char(string="Name", tracking=1)
    patient_id = fields.Many2one('hospital.patient')
    gender = fields.Selection(related='patient_id.gender', string="Gender", readonly=False)
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now, tracking=1)
    booking_date = fields.Date(string="Booking Date", tracking=1, default=fields.Date.context_today)
    doctor_id = fields.Many2one('res.users', string="Doctor", tracking=1)
    hospital_appointments_pharmacy_lines_ids= fields.One2many('hospital.appointments.pharmacy.lines','appointments_id')
    status = fields.Selection(
        [('draft', 'Draft'),
         ('in_process', 'In-Process'),
         ('done', 'Done'),
         ('cancel', 'Cancel'),
         ], default='draft',
    )
    Prescription=fields.Html()

    priority=fields.Selection(
        [
            ('0','low'),
            ('1','medium'),
            ('2','height')
        ]
    )
    Image=fields.Image(string="image" )


    hide_from_child=fields.Boolean(string="Hide from Child",default=False)

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


    def cancel_appointments(self):
        print(self.env.ref('hospital_managment.action_cancel_appointment_wizard'))
        action=self.env.ref('hospital_managment.action_cancel_appointment_wizard').read()[0]
        return action

class AppointmentsPharmacyLines(models.Model):
    _name = 'hospital.appointments.pharmacy.lines'
    _description = 'Appointments Pharmacy'

    name=fields.Char(string="Name")
    product_id = fields.Many2one('product.product')
    appointments_id = fields.Many2one('hospital.appointments',string="Appointments")
    qty=fields.Integer()
    price_unite=fields.Float(string="Unite Price")