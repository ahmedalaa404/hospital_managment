import datetime

from odoo import api, fields, models, _


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Patient Name",required=True)
    age = fields.Integer(string="age", compute='_compute_calc_age', store=True)
    ref = fields.Char(string="Reference",help="This refers to the patient is identity")
    active = fields.Boolean(string="active",default=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'FeMale'),
    ], string="gender", required=True, default='male')
    date_of_birth = fields.Date(string="Date of Birth")
    color=fields.Integer(string="Color",required=True)
    color2=fields.Char(string="Color2")

    tag_ids=fields.Many2many('hospital.patient.tag')
    
    @api.model
    def create(self, vals_list):
        vals_list['ref']=self.env['ir.sequence'].next_by_code('sequence.patient')
        return super(Patient,self).create(vals_list)

    def write(self,vals):
        if not self.ref or not vals.get('ref') :
           vals['ref']=self.env['ir.sequence'].next_by_code('sequence.patient')
        return super().write(vals)
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


    def name_get(self):
        patients_name=[]
        for rec in self:
            patients_name.append((rec.id,rec.name+rec.ref))

        return patients_name


