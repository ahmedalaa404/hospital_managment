# -*- coding: utf-8 -*-
# from odoo import http


# class OmHospitalEnhance(http.Controller):
#     @http.route('/om_hospital_enhance/om_hospital_enhance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_hospital_enhance/om_hospital_enhance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_hospital_enhance.listing', {
#             'root': '/om_hospital_enhance/om_hospital_enhance',
#             'objects': http.request.env['om_hospital_enhance.om_hospital_enhance'].search([]),
#         })

#     @http.route('/om_hospital_enhance/om_hospital_enhance/objects/<model("om_hospital_enhance.om_hospital_enhance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_hospital_enhance.object', {
#             'object': obj
#         })
