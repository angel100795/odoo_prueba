# -*- coding: utf-8 -*-
from odoo import http

# class OdooCurso/odooPractica(http.Controller):
#     @http.route('/odoo_curso/odoo_practica/odoo_curso/odoo_practica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_curso/odoo_practica/odoo_curso/odoo_practica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_curso/odoo_practica.listing', {
#             'root': '/odoo_curso/odoo_practica/odoo_curso/odoo_practica',
#             'objects': http.request.env['odoo_curso/odoo_practica.odoo_curso/odoo_practica'].search([]),
#         })

#     @http.route('/odoo_curso/odoo_practica/odoo_curso/odoo_practica/objects/<model("odoo_curso/odoo_practica.odoo_curso/odoo_practica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_curso/odoo_practica.object', {
#             'object': obj
#         })