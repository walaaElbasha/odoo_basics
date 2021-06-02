# -*- coding: utf-8 -*-
# from odoo import http


# class Medicine(http.Controller):
#     @http.route('/medicine/medicine/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/medicine/medicine/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('medicine.listing', {
#             'root': '/medicine/medicine',
#             'objects': http.request.env['medicine.medicine'].search([]),
#         })

#     @http.route('/medicine/medicine/objects/<model("medicine.medicine"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('medicine.object', {
#             'object': obj
#         })
