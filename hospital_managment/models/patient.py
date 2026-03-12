from odoo import api, fields, models, _


class Patient(models.Model):

    _name = 'hospital.patient'
    _description = 'Patient'

    name = fields.Char(string="Patient Name")
    age = fields.Integer(string="age")
    ref = fields.Char(string="Reference")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'FeMale'),
    ],string="gender")