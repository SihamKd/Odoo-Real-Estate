from odoo import models,fields

class Client(models.Model):
    _name = 'client'
    _description = "Client Model"
    _inherit = 'owner'