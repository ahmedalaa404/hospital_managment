from odoo import api, fields, models, _


class Patient(models.Model):

    _name = 'hospital.patient'
    _description = 'Patient'
    _inherit=['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Patient Name")
    age = fields.Integer(string="age")
    ref = fields.Char(string="Reference")
    active = fields.Boolean(string="active")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'FeMale'),
    ],string="gender",required=True,default='male')