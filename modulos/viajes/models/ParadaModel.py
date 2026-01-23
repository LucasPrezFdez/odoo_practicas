from odoo import fields, models, api

class Parada(models.Model):
    _name = "viajes.parada"
    _description = "Paradas de los Viajes"

    titulo = fields.Char(string="Titulo", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha = fields.Date(string="Fecha", default=fields.Date.today)
    duracion = fields.Float(digits=(5, 2), help="Duración en horas")
    localizacion = fields.Char(string="Localización")

    viaje_id = fields.Many2one('viajes.viaje', ondelete='cascade', string="Viaje", required=True)
    completada = fields.Boolean(string="Parada completada", default=False)

    @api.depends('completada')
    def marcar_completada(self):
        for record in self:
            record.completada = not record.completada

    mapa_embed = fields.Html(string="Mapa", compute="_compute_mapa_embed", sanitize=False)

    @api.depends('localizacion')
    def _compute_mapa_embed(self):
        for record in self:
            if record.localizacion:
                record.mapa_embed = f"""
                    <iframe width="100%" height="300" loading="lazy" 
                        src="https://www.google.com/maps?q={record.localizacion}&output=embed">
                    </iframe>
                """
            else:
                record.mapa_embed = "<p>Ubicación no disponible</p>"