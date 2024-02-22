# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ciclo(models.Model):
    _name = 'instituto.ciclo'
    _description = 'Ciclo'
    _rec_name="nombre"

    nombre = fields.Char()
    #Relacion uno a muchos con modulo
    modulos = fields.One2many('instituto.modulo','ciclo')