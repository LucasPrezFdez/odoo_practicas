from odoo import models, fields, api

class Vehiculo(models.Model):
    _name = 'viajes.vehiculo'
    _description = "viajes Vehiculo"
    modelo = fields.Char(string="Modelo", required=True)
    marca = fields.Char(string="Marca")
    descripcion = fields.Text()

     #Con la relación many2one me permite seleccionar un usuario o crearlo directamente
    propietario_id = fields.Many2one('res.users',
        ondelete='set null', string="Propietario", index=True)

    @api.depends('modelo', 'marca')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.modelo} - {record.marca}" if record.marca else record.modelo