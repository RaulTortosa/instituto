# -*- coding: utf-8 -*-
{
    'name': "Instituto",

    'summary': "Pequeño modulo para administrar un instituto",

    'description': """
Modulo para administrar los cursos, alumnos, profesores y asignaturas de un instituto
    """,

    'application': True,
    'author': "Raul Rodriguez Tortosa",
    'website': "https://github.com/RaulTortosa",
    'category': 'Productivity',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/ciclo.xml',
        'views/modulo.xml',
        'views/alumno.xml',
        'views/profesor.xml'
    ],
}
