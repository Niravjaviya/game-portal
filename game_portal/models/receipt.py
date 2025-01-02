from odoo import fields, models

class receipt (models.Model):
    _name = 'gaming.receipt'
    _description = 'Gaming receipt'
    _inherit = ['image.mixin']

    name= fields.Char(string='Name', required= True)
    user_id= fields.Many2one('res.users', string= 'Users')
    amount= fields.Float()
    account_id= fields.Many2one('res.partner.bank', string='Account')
    