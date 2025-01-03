from odoo import fields, models

class player (models.Model):
    _name = 'gaming.player'
    _description = 'Gaming player'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required= True)
    state= fields.Selection([('draft','Draft'),('active','Active'),('inactive','Inactive')],default='draft')
    wallet_id= fields.Many2one('gaming.wallet', string="Wallet")

    def status_active(self):
        self.state = 'active'

    def status_inactive(self):
        self.state = 'inactive'  

    