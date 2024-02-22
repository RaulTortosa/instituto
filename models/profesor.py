# -*- coding: utf-8 -*-

from odoo import models, fields, api


class profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'Profesor'
    _rec_name="nombre_completo"

    nombre = fields.Char()
    apellidos = fields.Char()
    dni = fields.Char(String="DNI")
    #Relacion uno a muchos con modulo
    modulos = fields.One2many('instituto.modulo','profesor')

    #Campo computado de nombre y apellido
    nombre_completo = fields.Char(compute='_compute_nombre_completo',store=True)
    #Funcion para concatenar nombre y apellido
    @api.depends('nombre', 'apellidos')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellidos}"