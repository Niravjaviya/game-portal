from odoo import fields, models

class wallet (models.Model):
    _name = 'gaming.wallet'
    _description = 'Gaming Wallet'

    name= fields.Char(string='Name', required= True)
    transaction_ids= fields.One2many('gaming.transaction','wallet_id', string='Transactions')
    user_id= fields.Many2one('res.users', string= 'Users')
    subscription_ids= fields.Many2many('gaming.subscription', string= 'Subscriptions')
    # deposit_ids= fields.
   