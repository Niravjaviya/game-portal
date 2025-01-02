from odoo import fields, models

class subscription (models.Model):
    _name = 'gaming.subscription'
    _description = 'Gaming subscription'

    name = fields.Char(string='Name', required= True)
    player_id = fields.Many2one('gaming.player',string='Players')
    product_id = fields.Many2one('product.product',string='Products')
    user_id= fields.Many2one('res.users', string= 'Users')
    transaction_ids= fields.One2many('gaming.transaction','wallet_id', string='Transactions')