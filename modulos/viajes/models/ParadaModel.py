from odoo import models, fields, api

class Parada(models.Model):
    _name = 'Paradas.parada'
    _description = "paradas Paradas"
    ciudad = fields.Char(string="Ciudad", required=True)
    calle = fields.Char(string="Calle")
    descripcion = fields.Text()

     #Con la relación many2one me permite seleccionar un usuario o crearlo directamente
    paradas_ids = fields.Many2one('res.paradas',
        ondelete='set null', string="Propietario", index=True)

    