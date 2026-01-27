from odoo import http
from odoo.http import request

class MiPrimerControlador(http.Controller):
    @http.route('/hola', auth='public', website=True)
    def hola_mundo(self):
        return "Hola desde el controlador de odoo"
    
    @http.route('/saludo', auth='public', website=True)
    def hola_mundo(self):
        return """
        <h1>Cebem</h1>
        <p>Hola desde Cebem SL</p>
        """
    
    @http.route('/saludo_plantilla', auth='public', website=True)
    def hola_mundo(self, **kw):
        return request.render('viajes.saludo')