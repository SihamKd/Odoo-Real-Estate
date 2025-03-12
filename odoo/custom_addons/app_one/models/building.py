from odoo import models,fields,api
from odoo.exceptions import ValidationError

class Building(models.Model):
    _name = 'building'
    _description = 'building'
    _inherit = ['mail.thread','mail.activity.mixin']
    #_rec_name = 'code' # this is the field that will be displayed (for reserved names) i used name instead this method

    no = fields.Integer()
    code = fields.Char()
    description = fields.Text()
    name = fields.Char()
    active = fields.Boolean(default=True) # this is to add archive functionality