# -*- coding: utf-8 -*-

from odoo import models, fields, api


class alumnos(models.Model):
    _name = 'instituto.alumno'
    _description = 'Alumno'
    _rec_name="nombre_completo"

    nombre = fields.Char()
    apellidos = fields.Char()
    dni = fields.Char(string="DNI")
    #Relacion muchos a muchos con modulo
    modulos = fields.Many2many('instituto.modulo')


    primerProfesor = fields.Many2one("instituto.profesor", related='modulos.profesor', string="Primer profesor", readonly=True)
    modulosProfe = fields.One2many('instituto.modulo',related='primerProfesor.modulos', string="Modulos 1er Profesor", readonly=True)

    #Campo computado de nombre y apellido
    nombre_completo = fields.Char(compute='_compute_nombre_completo',store=True)
    #Funcion para concatenar nombre y apellido
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"