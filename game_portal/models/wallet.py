from odoo import fields, models

class wallet (models.Model):
    _name = 'gaming.wallet'
    _description = 'Gaming Wallet'

    name= fields.Char(string='Name', required= True)
    state= fields.Selection([('draft','Draft'),('approved','Approved '),('pending','Pending'),('closed','Closed')],default='draft')
    transaction_ids= fields.One2many('gaming.transaction','wallet_id', string='Transactions')
    user_id= fields.Many2one('res.users', string= 'Users')
    subscription_ids= fields.Many2many('gaming.subscription', string= 'Subscriptions')
    # deposit_ids= fields.
   
    def status_approved(self):
        self.state = 'approved'

    def status_pending(self):
        self.state = 'pending'

    def status_closed(self):
        self.state = 'closed'    