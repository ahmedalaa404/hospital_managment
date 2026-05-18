from odoo import api, fields, models


class HospitalPatientTag(models.Model):
    _name = 'hospital.patient.tag'

    name = fields.Char(string="Name")
    color = fields.Integer(string="color picker")
    color_Picker2 = fields.Char(string="color_Picker2")
    active = fields.Boolean(default=True,copy=False)
    sequence = fields.Integer(default=0)
    def copy(self, default=None):
        default = dict(default or {})

        default.setdefault('name', f'{self.name}-(copy)')

        return super().copy(default)

    _sql_constraints = [
        ('unique_name', 'unique(name,active)', 'Name must be unique')
    ]


