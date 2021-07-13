# -*- coding: utf-8 -*-
# from odoo import http


# class DelphinusUpdate(http.Controller):
#     @http.route('/delphinus_update/delphinus_update/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delphinus_update/delphinus_update/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delphinus_update.listing', {
#             'root': '/delphinus_update/delphinus_update',
#             'objects': http.request.env['delphinus_update.delphinus_update'].search([]),
#         })

#     @http.route('/delphinus_update/delphinus_update/objects/<model("delphinus_update.delphinus_update"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delphinus_update.object', {
#             'object': obj
#         })
