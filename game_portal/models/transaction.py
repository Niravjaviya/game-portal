from odoo import fields, models

class transaction (models.Model):
    _name = 'gaming.transaction'
    _description = 'Gaming transaction'

    name= fields.Char(string='Name', required= True)
    wallet_id= fields.Many2one('gaming.wallet', string="Wallet")

    user_id= fields.Many2one('res.users', string="User")

    subcription_ids= fields.Many2one('gaming.subscription', string='Subscription')  
    account_id= fields.Many2one('res.partner.bank', string='Account')
    amount = fields.Float(string="Amount")
