from odoo import fields, models

class transaction (models.Model):
    _name = 'gaming.transaction'
    _description = 'Gaming transaction'
    _inherit = ['gaming.partner.mixin']

    name= fields.Char(string='Name', required= False)
    wallet_id= fields.Many2one('gaming.wallet', string="Wallet")

    # user_id= fields.Many2one('res.users', string="User")
    player_id = fields.Many2one('gaming.player',string='Players')
    subcription_ids= fields.Many2one('gaming.subscription', string='Subscription')  
    # account_id= fields.Many2one('res.partner.bank', string='Account')
    amount = fields.Float(string="Amount")
    transaction_type = fields.Selection([('add_money', 'Add Money'), ('withdraw', 'Withdraw')], string="Transaction Type")
    # add_money = fields.Float(string="Money Added", compute='_compute_add_money', store=True)

    # @api.depends('amount')
    # def _compute_add_money(self):
    #     for record in self:
    #         if record.transaction_type == 'add_money':
    #             record.add_money = record.amount
    #         else:
    #             record.add_money = 0.0
