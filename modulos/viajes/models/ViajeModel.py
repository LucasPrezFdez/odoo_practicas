from odoo import models, fields, api
from datetime import timedelta


class Viaje(models.Model):
    _name = 'viajes.viaje'
    _description = "Viajes"

    titulo = fields.Char(required=True)
    fecha_inicio = fields.Date(default=fields.Date.today)
    duracion = fields.Float(digits=(6, 2), help="Duracion en días")
    plazas = fields.Integer(string="Numero de plazas disponibles")

    estado = fields.Selection(
        selection=[
            ('planeado', 'Planeado'),
            ('en_curso', 'En curso'),
            ('finalizado', 'Finalizado')
        ],
        string="Estado",
        default="planeado",
        required=True
    )

    
    # En la relación many2one me permite elegir un partner/cliente o crear uno directamente
    conductor_id = fields.Many2one('res.partner', string="Conductor")

      
    # En la relación many2one me permite elegir un vehiculo o crear uno directamente
    vehiculo_id = fields.Many2one('viajes.vehiculo',
        ondelete='cascade', string="Vehiculo", required=True)