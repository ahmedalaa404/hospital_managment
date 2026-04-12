from odoo import api,fields,models

class HospitalPatientTag(models.Model):
    _name = 'hospital.patient.tag'

    name=fields.Char(string="Name")
    color=fields.Integer(string="color picker")
    color_Picker2=fields.Char(string="color_Picker2")