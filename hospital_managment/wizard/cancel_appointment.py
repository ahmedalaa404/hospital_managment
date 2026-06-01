from odoo import fields, models, api,_
from odoo.exceptions import ValidationError


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
        print(self.appointment_id.booking_date)
        print(fields.Date.today().today())
        cancel_day=self.env['ir.config_parameter'].get_param('hospital_managment.cancel_days')
        print("cancel_day",cancel_day)
        #
        # if self.appointment_id.booking_date== fields.Date.today().today():
        #     raise ValidationError(_("can`t remove any record from db in the same day"))
        #
