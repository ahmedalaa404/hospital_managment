from odoo import api, fields, models
from odoo.exceptions import UserError


class OdooPlayground(models.Model):
    _name = 'odoo.playground'
    _description = 'Odoo Playground'

    model_id = fields.Many2one(
        'ir.model',
        string='Model',

        ondelete='set null',
    )

    code = fields.Text(string='Code')
    result_code = fields.Text(string='Result Code', readonly=True)

    def action_clear(self):
        self.code = ''
        self.result_code = ''

    def action_excution(self):
        for rec in self:
            try:
                if not rec.model_id:
                    raise UserError("Please select a model.")

                model_name = rec.model_id.model
                model = self.env[model_name]

                localdict = {
                    'env': self.env,
                    'model': model,
                    'record': rec,
                    'result': '',
                }

                exec(rec.code or '', localdict)

                rec.result_code = str(localdict.get('result', 'Execution Done'))

            except Exception as e:
                rec.result_code = str(e)