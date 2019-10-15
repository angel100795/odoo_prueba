# -*- coding: utf-8 -*-

from odoo import models, fields, api,exceptions

class res_partner(models.Model):
	_name ='res.partner'
	_inherit = 'res.partner'
	company_type = fields.Selection(selection_add=[('is_school','Escuela'),('student','Estudiante')])
	student = fields.Many2one(
        'academia.student', 
        'Estudiante')

class academia_student(models.Model):
	_name = "academia.student"
	_description = "Modelo para formulacion de estudiantes"
	name = fields.Char('Nombre', size = 128,required = True)
	last_name = fields.Char('Apellido', size = 128)
	photo = fields.Binary('Fotografia')
	create_date = fields.Datetime('Fecha de creacion',readonly=True)
	note = fields.Html('Comentarios')
	active = fields.Boolean('Activo')
	age = fields.Integer ('Edad')
	curp = fields.Char('Curp', size=18)
	state = fields.Selection([('draf','Documento borrador'),('process','Proceso'),('done','Egresado',)],'Estado')
	##Relacionales
	partner_id = fields.Many2one('res.partner','Escuela')
	country = fields.Many2one('res.country','Pais', related='partner_id.country_id')
	calificaciones_id = fields.One2many('academia.calificacion','student_id','Calificaciones')

	@api.one 
	@api.constrains('curp')
	def _check_lines(self):
		if len(self.curp) < 18:
			raise exceptions.ValidationError("Curp debe ser de 18 caracteres.")

			
	_order = 'name'
	_defaults = {
		'active' : True,
    	'state' : 'draf',
    	}


# class odoo_curso/odoo_practica(models.Model):
#     _name = 'odoo_curso/odoo_practica.odoo_curso/odoo_practica'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100