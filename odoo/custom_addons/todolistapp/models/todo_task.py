from odoo import models, fields, api
from datetime import datetime

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To Do Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Task Name', required=True)
    assigned_to = fields.Many2one('res.users', string='Assign To')
    description = fields.Text(string='Description')
    due_date = fields.Date(string='Due Date', default=fields.Date.today)
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], string='Status', default='new', required=True, tracking=True)

    def action_in_progress(self):
        for rec in self:
            rec.status = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.status = 'completed'

    def action_new(self):
        for rec in self:
            rec.status = 'new'