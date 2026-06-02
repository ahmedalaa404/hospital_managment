from odoo import fields, models, api

class res_groups(models.Model):
    _inherit = 'res.groups'


    #this function used to hidden specification groups
    def get_application_groups(self, domain):
        """ Return the non-share groups that satisfy ``domain``. """
        return super().get_application_groups(domain)