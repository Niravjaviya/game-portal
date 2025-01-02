from odoo import fields, models

class deposit (models.Model):
    _name = 'gaming.deposit'
    _description = 'Gaming Deposit'

    name= fields.Char(string='Name', required= True)
    
    company_id = fields.Many2one(
        comodel_name='res.company',
        default=lambda self: self.env.company,
    )

    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    total_amount= fields.Monetary(string="Total Amount", currency_field='company_currency_id')


