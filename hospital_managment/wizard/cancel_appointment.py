from odoo import fields, models, api

class HospitalCancelAppointmentWizard(models.TransientModel):
    _name = 'hospital.cancel.appointment.wizard'
    _description = 'Cancel Appointment'

    name=fields.Char(string='Name')
    appointment_id=fields.Many2one('hospital.appointments')
    reason=fields.Char(string='Reason')
    def save(self):
        pass;