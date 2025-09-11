from odoo import models, fields,api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    property_id = fields.Many2one('property')
    #price = fields.Float(compute='_compute_price',store=True) 
    price = fields.Float(related ='property_id.selling_price') 


    #@api.depends('property_id')
    #def _compute_price(self):
     #   for record in self:
      #      record.price = record.property_id.selling_price
       #     print("Inside _compute_price")
        #    print(record.price)
    
