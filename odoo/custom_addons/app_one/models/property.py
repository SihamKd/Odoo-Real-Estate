from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import timedelta

class Property(models.Model):
    _name = 'property'
    _description = 'Property'
    _inherit = ['mail.thread','mail.activity.mixin']


    ref = fields.Char(default= "New", readonly=True)
    name = fields.Char(required=True, default="New",size=10)
    description = fields.Text(tracking=True)
    postcode = fields.Char(required=True)
    date_availability = fields.Date(tracking=True)
    expected_selling_date = fields.Date(tracking=True)
    is_late = fields.Boolean()
    expected_price = fields.Float()
    selling_price = fields.Float()
    diff=fields.Float(compute='_compute_diff',store = 1, readonly=False)
    bedrooms = fields.Integer(required=True)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean(groups="app_one.property_manager_group")
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ],default='north')


    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Name must be unique.')
    ]

    Line_ids = fields.One2many('property.line','property_id')   
    active = fields.Boolean(default=True)

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    owner_address = fields.Char(related='owner_id.address',readonly=True)
    owner_phone = fields.Char(related='owner_id.phone',readonly=True)
    create_time = fields.Datetime(default= fields.Datetime.now()) #default=fields.Datetime.now
    next_time = fields.Datetime(compute= '_compute_next_time')

    state =fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
        ('closed','Closed'),
    ],default ='draft')

    @api.depends('create_time')
    def _compute_next_time(self):
        for rec in self:
            if rec.create_time:
                rec.next_time = rec.create_time + timedelta(hours=6) 
            else:
                rec.next_time = False


    @api.depends('expected_price','selling_price')
    def _compute_diff(self):
        for rec in self:
            print("inside compute diff")
            #if record.expected_price and record.selling_price:
            rec.diff = rec.expected_price - rec.selling_price

    @api.onchange('expected_price','selling_price')
    def _onchange_expected_price(self):
        print("inside onchange")
        if self.expected_price and self.selling_price:
            self.diff = self.expected_price - self.selling_price
            return {
                'warning': {
                    'title': 'Warning',
                    'message': 'The expected price and selling price must be different.',
                    type: 'notification',
                },
            }

    @api.constrains('bedrooms')
    def _check_bedrooms(self):
        for record in self:
            if record.bedrooms == 0:
                raise ValidationError("Please enter a valid number of bedrooms.")
    
    def action_draft(self):
        for rec in self:
            rec.create_history_record(rec.state, 'draft')
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            rec.create_history_record(rec.state, 'pending')
            rec.write({
                'state':'pending'
            })#.write like rec.state the 2 are correct 

    def action_sold(self):
        for rec in self:
            rec.create_history_record(rec.state, 'sold')
            rec.state = 'sold'

    def action_closed(self):
        for rec in self:
            rec.create_history_record(rec.state, 'closed')
            rec.state = 'closed'

    def check_expected_selling_date(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.Date.today():
                rec.is_late = True

    def action(self):
        print(self.env['property'].search(['|',('name','=','property 1'),('postcode','!=','12345')])) #search for name = property 1 or postcode != 12345 , | is or , & is and , ! is not . 
    @api.model
    def create(self, vals):
        res = super(Property, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('property_seq')
        return res
    
    def create_history_record(self ,old_state, new_state , reason=""):
        for rec in self:
            rec.env['property.history'].create({
                'user_id': rec.env.uid,
                'property_id': rec.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason': reason or "",
                'line_ids': [(0, 0, {
                    'area': line.area,
                    'description': line.description,
                }) for line in rec.Line_ids],
            })

    def action_open_change_state_wizard(self):
        action= self.env['ir.actions.actions']._for_xml_id('app_one.change_state_wizard_action')
        action['context'] = {
            'default_property_id': self.id,
        }
        return action


""" to comment or #
     @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name'):
                vals['name'] = 'New'
                print("Creating data")
        return super().create(vals_list)
    

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        print("Searching data")
        return super()._search(domain, offset, limit, order, access_rights_uid)
    
    
    @api.model
    def write(self, vals):
        print("Writing data")
        return super().write(vals)
    

    def unlink(self):
        res = super(Property, self).unlink()
        print("Deleted successfully")
        return res
"""

class PropertyLine(models.Model):
    _name = 'property.line'
    _description = 'Property Line' 

    property_id = fields.Many2one('property')
    area = fields.Float()
    description = fields.Char()

