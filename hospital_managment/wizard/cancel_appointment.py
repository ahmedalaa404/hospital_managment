from dateutil.relativedelta import relativedelta

from odoo import fields, models, api,_
from odoo.exceptions import ValidationError
from odoo.fields import Date


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
        print("cancel_day",type(int(cancel_day)))
        allowed_date=self.appointment_id.booking_date - relativedelta(days=int(cancel_day))
        if allowed_date<Date.today():
            raise ValidationError(_('Cancel appointment date cannot be in the past'))
        self.appointment_id.state='cancel'
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

