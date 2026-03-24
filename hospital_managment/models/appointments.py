from odoo import fields,models

class Appointments(models.Model):
    _name = 'hospital.appointments'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Appointments'

    name=fields.Char(string="Name",tracking=1)
    patient_id=fields.Many2one('hospital.patient')
    appointment_time=fields.Datetime(string="Appointment Time",default=fields.Datetime.now,tracking=1)
    booking_date=fields.Date(string="Booking Date",tracking=1,default=fields.Date.context_today)