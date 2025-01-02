from odoo import fields, models

class player (models.Model):
    _name = 'gaming.player'
    _description = 'Gaming player'

    name= fields.Char(string='Name', required= True)
    wallet_id= fields.Many2one('gaming.wallet', string="Wallet")
    