import datetime

from odoo import api, fields, models, _


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Patient Name")
    age = fields.Integer(string="age", compute='_compute_calc_age', store=True)
    ref = fields.Char(string="Reference",help="This refers to the patient is identity")
    active = fields.Boolean(string="active")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'FeMale'),
    ], string="gender", required=True, default='male')
    date_of_birth = fields.Date(string="Date of Birth")
    color=fields.Integer(string="Color")
    color2=fields.Char(string="Color2")

    tag_ids=fields.Many2many('hospital.patient.tag')

    @api.depends('date_of_birth')
    def _compute_calc_age(self):
        for rec in self:
            if rec.date_of_birth:
                year_of_now=datetime.datetime.now().year
                year_of_birth=rec.date_of_birth.year
                print(year_of_birth)
                print(year_of_now)
                rec.age = year_of_now - year_of_birth
            else:
                rec.age = 0

