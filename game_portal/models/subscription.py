from odoo import fields, models, api

class subscription (models.Model):
    _name = 'gaming.subscription'
    _description = 'Gaming subscription'
    _inherit = ['mail.thread', 'mail.activity.mixin','gaming.partner.mixin']


    name = fields.Char(string='Name', required= True)
    state= fields.Selection([('draft','Draft'),('subscribed','Subscribed'),('pending','Pending')],default='draft')
    player_id = fields.Many2one('gaming.player',string='Players')
    product_id = fields.Many2one('product.product',string='Products')
    # user_id= fields.Many2one('res.users', string= 'Users')
    transaction_ids= fields.One2many('gaming.transaction','wallet_id', string='Transactions')

    def status_subscribed(self):
        self.state = 'subscribed'

    def status_pending(self):
        self.state = 'pending'


    company_id = fields.Many2one(
        comodel_name='res.company',
        default=lambda self: self.env.company,
    )
    company_currency = fields.Many2one("res.currency", string='Currency', related='company_id.currency_id')
    total_amount = fields.Monetary(string='Total Transaction Amount', compute='_compute_total_amount', store=False, currency_field='company_currency')
    

    @api.depends('transaction_ids.amount')
    def _compute_total_amount(self):
        for subscription in self:
            # Sum the amounts from related transactions
            subscription.total_amount = sum(transaction.amount for transaction in subscription.transaction_ids)