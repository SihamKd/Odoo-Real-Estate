from odoo import models,fields,api
from odoo.exceptions import ValidationError

class Tag(models.Model):
    _name = 'tag'
    _description = 'tag'

    name = fields.Char(required=True)

    