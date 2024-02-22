# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modulo(models.Model):
    _name = 'instituto.modulo'
    _description = 'Modulo'
    _rec_name="nombre"

    nombre = fields.Char()
    #Relacion uno a muchos con ciclo y profesor
    ciclo = fields.Many2one(comodel_name="instituto.ciclo")
    profesor = fields.Many2one(comodel_name="instituto.profesor")
    #Relacion muchos a muchos con alumnos
    alumnos = fields.Many2many('instituto.alumno')
