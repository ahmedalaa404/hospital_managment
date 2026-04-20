from odoo import fields, models, api


class HospitalCancelAppointmentWizard(models.TransientModel):
    _name = 'hospital.cancel.appointment.wizard'
    _description = 'Cancel Appointment'

    @api.model
    def default_get(self, fields_list):

        result = super(HospitalCancelAppointmentWizard, self).default_get(fields_list)
        result['reason']="Try to set default value of reason without add attribute in fields"
        return result

    name = fields.Char(string='Name',default="test name for cancel appointment")
    appointment_id = fields.Many2one('hospital.appointments')
    reason = fields.Char(string='Reason')

    def save(self):
        pass;
