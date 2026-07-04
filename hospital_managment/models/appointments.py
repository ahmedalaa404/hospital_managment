from odoo import fields, models, api, _
from odoo.api import ondelete
from odoo.exceptions import ValidationError


class Appointments(models.Model):
    _name = 'hospital.appointments'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Appointments'
    _rec_name = 'gender'
    _order = 'id desc'

    name = fields.Char(string="Name", tracking=1)
    patient_id = fields.Many2one('hospital.patient', ondelete='restrict')
    ref = fields.Char(related='patient_id.ref')
    gender = fields.Selection(related='patient_id.gender', string="Gender", readonly=False)
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now, tracking=30)
    booking_date = fields.Date(string="Booking Date", tracking=10, default=fields.Date.context_today)
    doctor_id = fields.Many2one('res.users', string="Doctor", tracking=10)
    hospital_appointments_pharmacy_lines_ids = fields.One2many('hospital.appointments.pharmacy.lines',
                                                               'appointments_id')
    status = fields.Selection(
        [('draft', 'Draft'),
         ('in_process', 'In-Process'),
         ('done', 'Done'),
         ('cancel', 'Cancel'),
         ], default='draft',
    )
    Prescription = fields.Html()
    duration = fields.Integer()

    priority = fields.Selection(
        [
            ('0', 'low'),
            ('1', 'medium'),
            ('2', 'height')
        ]
    )
    Image = fields.Image(string="image")
    operation_id = fields.Many2one('operation.operation')
    progress = fields.Integer(string="progress", compute='_compute_progress')

    hide_from_child = fields.Boolean(string="Hide from Child", default=False)
    company_id = fields.Many2one('res.company', 'company', default=lambda self: self.env.company)
    # currency_id=fields.Many2one('res.currency','currency',default=lambda self:self.env.company.currency_id)
    currency_id = fields.Many2one('res.currency', 'currency', related='company_id.currency_id')

    def unlink(self):
        if self.status == 'done':
            raise ValidationError(_("you can`t do it , state is done "))
        return super().unlink()

    def action_test(self):
        return {
            'type': 'ir.actions.act_url',
            'target': '_blank',
            'url':'www.google.com'
            # 'effect': {
            #     'message': "test action for rainbow man ",
            #     'type': 'rainbow_man',
            #     'fadeout': 'slow'
            # }
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
        action = self.env.ref('hospital_managment.action_cancel_appointment_wizard').read()[0]
        action['context'] = {'default_appointment_id': self.id, 'hide_appointment_id': 1}
        return action

    # functions set specification state
    def actions_set_status_cancel(self):
        print("server action")
        self.write({'status': 'cancel'})

    def action_set_done(self):
        for rec in self:
            rec.status = 'done'
            print(rec)

    @api.depends('status')
    def _compute_progress(self):
        for rec in self:
            if rec.status == 'draft':
                rec.progress = 25
            elif rec.status == 'in_process':
                rec.progress = 50
            elif rec.status == 'done':
                rec.progress = 100
            elif rec.status == 'cancel':
                rec.progress = 0

    def share_whatsapp(self):
        print("share_whatsapp")
        if not self.patient_id.phone:
            raise ValidationError(_('Must be patient have Phone to allow to send message whatsapp'))
        url_whatsapp_api=f'https://api.whatsapp.com/send?phone={self.patient_id.phone}&text=appointments'

        return {
            'type':'ir.actions.act_url',
            'target':'_blank',
            'url':f"{url_whatsapp_api}"
        }
    def test_case(self):
        data_search_it=self.search([],limit=10,order='id desc')
        print("Meta Data ->>> ",self.get_metadata()[0])
        print("search count without Domain have limit and order only",data_search_it)
        print("Fields Parameter",self.fields_get())

class AppointmentsPharmacyLines(models.Model):
    _name = 'hospital.appointments.pharmacy.lines'
    _description = 'Appointments Pharmacy'

    name = fields.Char(string="Name")
    product_id = fields.Many2one('product.product')
    appointments_id = fields.Many2one('hospital.appointments', string="Appointments")
    qty = fields.Integer()
    price_unite = fields.Float(string="Unite Price")
    company_currency_id = fields.Many2one('res.currency', 'currency', related='appointments_id.currency_id')
    price_subtotal = fields.Monetary(string="Subtotal", compute="_compute_price_subtotal",
                                     currency_field='company_currency_id')

    @api.depends('price_unite', 'qty')
    def _compute_price_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.price_unite * rec.qty




    def share_whatsapp(self):
            return {
                'type': 'ir.actions.act_url',
                'target': '_blank',
                'url': 'url go to for this ',
            }




