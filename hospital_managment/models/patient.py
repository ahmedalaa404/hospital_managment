from calendar import month

from odoo import api, fields, models, _

from odoo.exceptions import ValidationError
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Patient Name", required=True)
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="age", compute='_compute_calc_age', inverse='_inverse_compute_age',search='_search_age')
    ref = fields.Char(string="Reference", help="This refers to the patient is identity")
    active = fields.Boolean(string="active", default=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'FeMale'),
    ], string="gender", required=True, default='male')

    color = fields.Integer(string="Color", required=True)
    color2 = fields.Char(string="Color2")

    tag_ids = fields.Many2many('hospital.patient.tag')

    appointments_ids = fields.One2many('hospital.appointments', 'patient_id', string="Appointments")
    appointments_count = fields.Integer(string="Appointments Count", compute="_compute_appointments_count", store=True)

    parent = fields.Char(string="Parent Patient")
    partner_name = fields.Char(string="partner name")
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ], string="Marital Status")

    @api.depends('appointments_ids')
    def _compute_appointments_count(self):
        for rec in self:
            rec.appointments_count = self.env['hospital.appointments'].search_count(
                [('patient_id', '=', rec.id)])

    @api.model
    def create(self, vals_list):
        vals_list['ref'] = self.env['ir.sequence'].next_by_code('sequence.patient')
        return super(Patient, self).create(vals_list)

    def write(self, vals):
        if not self.ref or not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('sequence.patient')
        return super().write(vals)

    @api.depends('date_of_birth')
    def _compute_calc_age(self):
        for rec in self:
            if rec.date_of_birth:
                year_of_now = datetime.now().year
                year_of_birth = rec.date_of_birth.year
                print(year_of_birth)
                print(year_of_now)
                rec.age = year_of_now - year_of_birth
            else:
                rec.age = 0

    def name_get(self):
        patients_name = []
        for rec in self:
            name = rec.name + " " + rec.ref
            patients_name.append((rec.id, name))

        return patients_name

    def default_get(self, fields_list):
        print(fields_list)
        return super(Patient, self).default_get(fields_list)

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today() and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The Enter data is Not acceptable"))

    @api.model
    def default_get(self, fields_list):
        print(self)
        print(fields_list)
        return super().default_get(fields_list)

    @api.ondelete(at_uninstall=False)
    def check_appointments(self):
        for rec in self:
            if rec.appointments_ids:
                raise ValidationError(_("U Can`t delete patient if have appointments"))

    def action_appear_group_by(self):
        for rec in self:
            print(rec)

    @api.onchange('age')
    @api.depends('age')
    def _inverse_compute_age(self):
        for rec in self:
            if rec.age:
                rec.date_of_birth = date.today() - relativedelta(years=rec.age)


    def _search_age (self, operator,value):
        print("-------------------------------------------------------")
        print(operator)
        print(value)
        start_date=(date.today() - relativedelta(years=value)).replace(day=1,month=1)
        end_date=(date.today() - relativedelta(years=value)).replace(day=31,month=12)
        print("----start_date-----",start_date)
        print("----end_date-----",end_date)
        print("-------------------------------------------------------")

        # start_date=date.date(month=1,days=1)
        return [('date_of_birth','>=',start_date),('date_of_birth','<=',end_date)]